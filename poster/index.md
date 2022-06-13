# oneAPI for Scientific Python Community
by Diptorup Deb and Oleksandr Pavlyk, Intel Corp.

## What is oneAPI?

[oneAPI][oneAPI] is an open standard for a unified application
programming interface (API) that delivers a common developer experience across
accelerator architectures, including multi-core CPUs, GPUs, and FPGAs.

A freely available implementation of the standard is available through
[Intel(R) oneAPI Toolkits][toolkits]. The [Intel(R) Base Toolkit][basekit] features
an industry-leading C++ compiler that implements [SYCL*][sycl], an evolution of C++
for heterogeneous computing. It also includes a suite of performance libraries, such as
Intel(R) oneAPI Math Kernel Library ([oneMKL][oneMKL]), etc, as well as
[Intel(R) Distribution for Python*][idp].

```{image} _static/oneapi_basekit.webp
:alt: Intel oneAPI Base Toolkit
:width: 1072px
:align: center
```

```{note} **TODO**
Explain anatomy of DPC++ executable, and [layered architecture of oneAPI][layered-architecture].
```

```{note} **TODO**
Python extensions created by DPC++.
```

```{note} **TODO**
Explain intel/llvm support for [multiple backends][sycl-five-additions].
```

## Additional information

[Data Parallel C++ book][dpcpp-book] is an excellent resource to get familiar with programming
heterogeneous systems using C++ and SYCL*.

Intel(R) DevCloud hosts [base training material][base-training-modules] which can be executed
on the variety of Intel(R) hardware using preinstalled oneAPI toolkits.

Julia support for oneAPI.

[oneAPI]: https://www.oneapi.io
[toolkits]: https://www.intel.com/content/www/us/en/developer/tools/oneapi/toolkits.html
[basekit]: https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html
[sycl]: https://www.khronos.org/sycl/
[oneMKL]: https://www.intel.com/content/www/us/en/develop/documentation/oneapi-programming-guide/top/api-based-programming/intel-oneapi-math-kernel-library-onemkl.html
[idp]: https://www.intel.com/content/www/us/en/developer/tools/oneapi/distribution-for-python.html
[layered-architecture]: https://www.intel.com/content/www/us/en/developer/articles/technical/expanding-oneapi-support-for-languages-and-accelerators.html
[sycl-five-additions]: https://www.intel.com/content/www/us/en/developer/articles/technical/five-outstanding-additions-sycl2020.html
[base-training-modules]: https://devcloud.intel.com/oneapi/get_started/baseTrainingModules/
[dpcpp-book]: https://link.springer.com/book/10.1007%2F978-1-4842-5574-2
