---
title: Why use oneAPI in Python
markup: 
    TableOfContents:
        endLevel: 3
        ordered: false
        startLevel: 2
type: docs
weight: 50
---


Here is a summary of why we think Scientific Python community should embrace oneAPI

1. oneAPI is an open, cross-industry, standards-based, unified, multiarchitecture, multi-vendor [programming model][oneAPI-wiki]. 
2. DPC++ compiler is being developed in open-source, see http://github.com/intel/llvm, and is being upstreamed into LLVM project itself.
3. Open source compiler supports [variety of backends][sycl-five-additions], including oneAPI [Level-Zero][l0], [OpenCL(TM)][ocl], NVIDIA(R) [CUDA(R)][cuda], and [HIP][hip].
4. [oneAPI Math Kernel Library (oneMKL) Interfaces](https://github.com/oneapi-src/oneMKL) supports a collection of third-party libraries associated with 
supported backends permitting portability.

With these features in mind, and DPC++ runtime being compatible with compiler toolchain used to build CPython itself, use of oneAPI 
promises to enable Python extensions to leverage a variety of accelerators, while maintaining portability 
of Python extensions across different heterogenous systems, from HPC clusters and servers to laptops.

[sycl-five-additions]: https://www.intel.com/content/www/us/en/developer/articles/technical/five-outstanding-additions-sycl2020.html
[l0]: https://spec.oneapi.io/level-zero/latest/index.html
[ocl]: https://www.khronos.org/opencl/
[cuda]: https://developer.nvidia.com/cuda-toolkit
[hip]: https://github.com/ROCm-Developer-Tools/HIP
[oneAPI-wiki]: https://en.wikipedia.org/wiki/OneAPI_(compute_acceleration)
