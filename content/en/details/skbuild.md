---
title: "oneAPI Python extensions"
date: 2022-06-14
type: docs
weight: 40
description: >
  Python extensions can be built with DPC++. This is how.
---

### Suitability of DPC++ for Python stack

DPC++ is a [single source compiler][dpcpp-single-source]. It generates [both the host code and the device code][compilation-flow] in a single fat binary.

DPC++ is an LLVM-based compiler, but the host portion of the binary it produces is compatible with GCC runtime libraries on Linux and Windows runtime libraries on Windows. Thus, native Python extensions authored in C++ can be directly built with DPC++. Such extensions will require DPC++ runtime library at the runtime.

Intel(R) compute runtime needs to be present for DPC++ runtime to be able to target supported Intel devices. When using open-source DPC++ from [github.com/intel/llvm][intel-llvm] compiled with support for NVIDIA CUDA, HIP NVIDIA, or HIP AMD (see [intel/llvm/getting-started][intel-llvm-getting-started] for details), respective runtimes and drivers will need to be present for DPC++ runtime to target these devices.

### Build a data-parallel Python native extension

There are two supported ways of building a data-parallel extension: by using
`Cython` and by using `pybind11`. The companion repository
[IntelPython/sample-data-parallel-extensions][sample-dppy-ext] provides the
examples demonstrating both approaches by implementing two prototype native
extensions to evaluate [Kernel Density Estimate][wiki-kde]
at a set a points from a Python function with the following signature:

```python
def kde_eval(exec_q: dpctl.SyclQueue, x : np.ndarray, data: np.ndarray, h : float) -> np.narray: ...
    """
    Args:
       q: execution queue specifying offload target
       x: NumPy array of shape (n, dim)
       d: NumPy array of shape (n_data, dim)
       h: moothing parameter
    """
```

The examples can be cloned locally using git:

```bash
git clone https://github.com/IntelPython/sample-data-parallel-extensions.git
```

The examples demonstrate a key benefit of using the `dpctl` package and the
included `Cython` and `pybind11` bindings for oneAPI. By using `dpctl`,
a native extension writer can focus on writing a data-parallel kernel in DPC++
while automating the generation of the necessary Python bindings using `dpctl`.

#### Building packages with setuptools

When using `setuptools` we [used][kde-setuptools] environment variables `CC` and
`LDSHARED` recognized by `setuptools` to ensure that `dpcpp` is used to compile
and link extensions.

The resulting extension is a fat binary, containing both the host code with
Python bindings and offloading orchestration, and the device code usually stored
in cross-platform intermediate representation (SPIR-V) and compiled for the
device indicated via the execution queue argument using tooling from compute
runtime.

#### Building packages with scikit-build

Using setuptools is convenient, but may feel klunky. Using
[scikit-build][scikit-build] offers an alternate way for users who prefer or are
familiar with `CMake`.

Scikit-build enables writing the logic of Python package building in CMake which [supports oneAPI DPC++][cmake-dpcpp]. Scikit-build supports building of both
Cython-generated and pybind11-generated native extensions. `dpctl` integration with CMake allows to conveniently using `dpctl` integration with these extension generators
simply by including

```cmake
find_package(Dpctl REQUIRED)
```

In order for CMake to locate the script that would make the example work, the
example `CMakeLists.txt` in [`kde_skbuild`][kde-skbuild] package implements
`DPCTL_MODULE_PATH` variable which can be set to output of `python -m dpctl
--cmakedir`. Integration of DPC++ with CMake requires that CMake's C and/or C++
compiler were set to Intel LLVM compilers provided in oneAPI base kit.

```bash
python setup.py develop -G Ninja -- \
    -DCMAKE_C_COMPILER=icx          \
    -DCMAKE_CXX_COMPILER=icpx       \
    -DDPCTL_MODULE_PATH=$(python -m dpctl --cmakedir)
```

Alteratively, we can rely on CMake recognizing `CC` and `CXX` environment variables to shorten the input

```
CC=icx CXX=icpx python setup.py develop -G Ninja -- -DDCPTL_MODULE_PATH=$(python -m dpctl --cmakedir)
```


Whichever way of building the data-parallel extension appeals to you, the end
result allows offloading computations specified as DPC++ kernels to any
supported device:

```ipython
import dpctl
import numpy as np
import kde_skbuild as kde

cpu_q = dpctl.SyclQueue("cpu")
gpu_q = dpctl.SyclQueue("gpu")

# output info about targeted devices
cpu_q.print_device_info()
gpu_q.print_device_info()

x = np.linspace(0.1, 0.9, num=14000)
data = np.random.uniform(0, 1, size=10**6)

# Notice that first evaluation results in JIT-compiling the kernel
# Subsequent evaluation reuse cached binary
f0 = kde.cython_kde_eval(cpu_q, x[:, np.newaxis], data[:, np.newaxis], 3e-6)

f1 = kde.cython_kde_eval(gpu_q, x[:, np.newaxis], data[:, np.newaxis], 3e-6)

assert np.allclose(f0, f1)
```

The following naive NumPy implementation can be used to validate the results
generated by our sample extensions. Do note that the validation script would
not be able to handle very large size inputs and will raise a `MemoryError`
exception.

```
def ref_kde(x, data, h):
    """
    Reference NumPy implementation for KDE evaluation
    """
    assert x.ndim == 2 and data.ndim == 2
    assert x.shape[1] == data.shape[1]
    dim = x.shape[1]
    n_data = data.shape[0]
    return np.exp(
        np.square(x[:, np.newaxis, :]-data).sum(axis=-1)/(-2*h*h)
    ).sum(axis=1)/(np.sqrt(2*np.pi)*h)**dim / n_data
```

Using CPU offload target allows to parallelize CPU computations. For example, try

```ipython
data = np.random.uniform(0, 1, size=10**3)
x = np.linspace(0.1, 0.9, num=140)
h = 3e-3

%time fr = ref_kde(x[:,np.newaxis], data[:, np.newaxis], h)
%time f0 = kde_skbuild.cython_kde_eval(cpu_q, x[:, np.newaxis], data[:, np.newaxis], h)
%time f1 = kde_skbuild.cython_kde_eval(gpu_q, x[:, np.newaxis], data[:, np.newaxis], h)

assert np.allclose(f0, fr) and np.allclose(f1, fr)
```

`dpctl` can be used to build data-parallel Python extensions which functions operating of USM-based arrays.
For example, please refer to [examples/pybind11/onemkl_gemv][onemkl-gemv] in dpctl sources.


[dpcpp-single-source]: https://oneapi-src.github.io/DPCPP_Reference/#data-parallel-c-dpc
[compilation-flow]: https://www.intel.com/content/www/us/en/develop/documentation/oneapi-programming-guide/top/programming-interface/compilation-flow-overview.html
[intel-llvm]: https://github.com/intel/llvm.git
[intel-llvm-getting-started]: https://github.com/intel/llvm/blob/sycl/sycl/doc/GetStartedGuide.md
[sample-dppy-ext]: https://github.com/IntelPython/sample-data-parallel-extensions
[wiki-kde]: https://en.wikipedia.org/wiki/Kernel_density_estimation
[kde-setuptools]: https://github.com/IntelPython/sample-data-parallel-extensions/tree/main/kde_setuptools
[kde-skbuild]: https://github.com/IntelPython/sample-data-parallel-extensions/tree/main/kde_skbuild
[scikit-build]: https://github.com/scikit-build/scikit-build
[cmake-dpcpp]: https://www.intel.com/content/www/us/en/develop/documentation/oneapi-dpcpp-cpp-compiler-dev-guide-and-reference/top/compiler-setup/use-the-command-line/use-cmake-with-the-intel-oneapi-dpc-c-compiler.html
[onemkl-gemv]: https://github.com/IntelPython/dpctl/tree/master/examples/pybind11/onemkl_gemv
