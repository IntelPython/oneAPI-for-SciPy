---
title: "What is oneAPI"
date: 2022-06-14
type: docs
weight: 10
description: >
  oneAPI - the standard and its implementation.
---

[oneAPI][oneAPI] is an open standard for a unified application
programming interface (API) that delivers a common developer experience across
accelerator architectures, including multi-core CPUs, GPUs, and FPGAs.

### Toolkits

A freely available implementation of the standard is available through
[Intel(R) oneAPI Toolkits][toolkits]. The [Intel(R) Base Toolkit][basekit] features
an industry-leading C++ compiler that implements [SYCL*][sycl], an evolution of C++
for heterogeneous computing. It also includes a suite of performance libraries, such as
Intel(R) oneAPI Math Kernel Library ([oneMKL][oneMKL]), etc, as well as
[Intel(R) Distribution for Python*][idp].

![Intel Base Toolkit][1]

[1]: ../../images/oneapi_basekit.webp "Composition of Intel Base Toolkit"

DPC++ is a LLVM-based compiler project that implements compiler and runtime support for SYCL* language.
It is being developed in `sycl` branch of the LLVM project fork [github.com/intel/llvm][intel-llvm].
The project publishes [daily builds][llvm-daily-prereleases] for Linux.

Intel(R) oneAPI DPC++ compiler is a proprietary product that builds on the open-source DPC++ project.
It is part of Intel(R) compiler suite which has completed the [adoption of LLVM infrastructure][icx-adopts-llvm] and is available in oneAPI toolkits.
In particular, Intel(R) Fortran compiler is freely avialable on all supported platforms in [Intel(R) oneAPI HPC Toolkit][hpckit].

DPC++ leverages standard toolchain runtime libraries, such as `glibc` and `libstdc++` on Linux and `wincrt` on Windows. This makes it possible to use
Intel C/C++ compilers, including DPC++, to compile Python [native extensions](skbuild.mc) compatible with the CPython and the rest of Python stack.

In order to enable cross-architecture programming for CPUs and accelerators the DPC++ runtime adopted [layered architecture][layered-architecture].
Software concepts are mapped to hardware abstraction layer by user-specified [SYCL backend][sycl-five-additions] which programs the specific hardware in use.

### Compute runtime

An integral part of this layered architecture is provided by [Intel(R) Compute Runtime][compute-runtime]. oneAPI application is a fat binary consisting of
device codes in a standardized intermediate form [SPIR-V][spriv] and host code which orchestrates tasks such as querying of the heterogeneous system it is
running on, selecting accelerator(s), compiling (jitting) device code in the intermediate representation for the selected device, managing device memory, and
submitting compiled device code for execution. The host code performs these tasks by using DPC++ runtime, which maps them to hardware abstraction layer, that
talks to hardware-specific drivers.

![working of oneAPI executable](../../images/oneAPI-executable-diagram.webp)

### Additional information

[Data Parallel C++ book][dpcpp-book] is an excellent resource to get familiar with programming
heterogeneous systems using C++ and SYCL*.

Intel(R) DevCloud hosts [base training material][base-training-modules] which can be executed
on the variety of Intel(R) hardware using preinstalled oneAPI toolkits.

Julia has support for oneAPI [github.com/JuliaGPU/oneAPI.jl][julia-oneAPI].


[oneAPI]: https://www.oneapi.io
[toolkits]: https://www.intel.com/content/www/us/en/developer/tools/oneapi/toolkits.html
[basekit]: https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html
[hpckit]: https://www.intel.com/content/www/us/en/developer/tools/oneapi/hpc-toolkit.html
[sycl]: https://www.khronos.org/sycl/
[oneMKL]: https://www.intel.com/content/www/us/en/develop/documentation/oneapi-programming-guide/top/api-based-programming/intel-oneapi-math-kernel-library-onemkl.html
[idp]: https://www.intel.com/content/www/us/en/developer/tools/oneapi/distribution-for-python.html
[layered-architecture]: https://www.intel.com/content/www/us/en/developer/articles/technical/expanding-oneapi-support-for-languages-and-accelerators.html
[sycl-five-additions]: https://www.intel.com/content/www/us/en/developer/articles/technical/five-outstanding-additions-sycl2020.html
[base-training-modules]: https://devcloud.intel.com/oneapi/get_started/baseTrainingModules/
[dpcpp-book]: https://link.springer.com/book/10.1007%2F978-1-4842-5574-2
[julia-oneAPI]: https://github.com/JuliaGPU/oneAPI.jl
[intel-llvm]: https://github.com/intel/llvm.git
[icx-adopts-llvm]: https://www.intel.com/content/www/us/en/developer/articles/technical/adoption-of-llvm-complete-icx.html
[llvm-daily-prereleases]: https://github.com/intel/llvm/releases
[compute-runtime]: https://github.com/intel/compute-runtime.git
[spriv]: https://www.khronos.org/spir/
