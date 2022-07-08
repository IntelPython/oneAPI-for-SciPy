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

DPC++ is an LLVM-based compiler, but the host portion of the binary it produces is compatible with GCC runtime libraries on Linux and Windows runtime libraries on Windows. Thus native Python extensions authored in C++ can be directly built with DPC++. Such extensions will require DPC++ runtime library at the runtime. 

Intel(R) compute runtime needs to be present for DPC++ runtime to be able to target supported Intel devices. When using open-source DPC++ from [github.com/intel/llvm][intel-llvm] compiled with support for NVIDIA CUDA, HIP NVIDIA, or HIP AMD (see [intel/llvm/getting-started][intel-llvm-getting-started] for details), respective runtimes and drivers will need to be present for DPC++ runtime to target these devices.

### Examples of data-parallel extensions

Here we present two ways of building data-parallel extensions illustrated in a companion 
repo [IntelPython/sample-data-parallel-extensions][sample-dppy-ext].

Each extension within respective packages implements data-parallel Python functions to evaluate [Kernel Density Estimate][wiki-kde] at a set a points with signature:

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

Within each package one extension is built using `Cython` and another using `pybind11` extension generators. This way author of data-parallel extension can focus
on writing data-parallel code in DPC++ while automating generation of necessary Python bindings.

#### Building packages with setuptools

When using setuptools we [used][kde-setuptools] environment variables `CC` and `LDSHARED` recognized by `setuptools` to ensure that `dpcpp` is used to compile and link extensions. 

The resulting extension is a fat binary, containing both the host code with Python bindings and offloading orchestration, and the device code usually stored 
in cross-platform intermediate representation (SPIR-V) and compiled for the device indicated via the execution queue argument using tooling from compute runtime.

#### Building packages with scikit-build

Using setuptools is convenient, but feels klunky. Enter [scikit-build][scikit-build].

Scikit-build enables writing the logic of Python package building in CMake which [supports oneAPI DPC++][cmake-dpcpp]. Scikit-build supports building of both
Cython-generated and pybind11-generated native extensions. `dpctl` integration with CMake allows to conveniently using `dpctl` integration with these extension generators
simply by including 

```cmake
find_package(Dpctl REQUIRED)
```

In order for CMake to locate the script that would make this work the example `CMakeLists.txt` in [`kde_skbuild`][kde-skbuild] package implements `DPCTL_MODULE_PATH` variable 
which can be set to output of `python -m dpctl --cmakedir`. Integration of DPC++ with CMake requires that CMake's C and/or C++ compiler were set to Intel LLVM compilers
provided in oneAPI base kit.

```bash
python setup.py develop -G Ninja -- \
    -DCMAKE_C_COMPILER=icx          \
    -DCMAKE_CXX_COMPILER=icpx       \
    -DDPCTL_MODULE_PATH=$(python -m dpctl --cmakedir)
```

Altenatively, we can rely on CMake recognizing `CC` and `CXX` environment variables to shorten the input

```
CC=icx CXX=icpx python setup.py develop -G Ninja -- -DDCPTL_MODULE_PATH=$(python -m dpctl --cmakedir)
```


Whichever way of build the data-parallel extension apeals to you, the end result allows to offload certain computations for any of the supported devices:

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

Of course a naive NumPy reference implementation can not handle the large size input like used above, running out of memory,
but it can be used to confirm correctness:

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
