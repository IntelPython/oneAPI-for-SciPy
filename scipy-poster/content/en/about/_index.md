---
title: Why should Scientific Python community should embrace oneAPI
linkTitle: About
menu:
  main:
    weight: 10

---

1. oneAPI is an open, cross-industry, standards-based, unified, multiarchitecture, multi-vendor programming model.
2. DPC++ compiler is being developed in open-source, see http://github.com/intel/llvm, and is being upstreamed into LLVM project itself.
3. Open source compiler supports [variety of backends][sycl-five-additions], including [Level-Zero][l0], [OpenCL][ocl], [CUDA][cuda], and [HIP][hip].
3. [oneAPI Math Kernel Library (oneMKL) Interfaces](https://github.com/oneapi-src/oneMKL) supports a collection of third-party libraries associated with supported backends.

[sycl-five-additions]: https://www.intel.com/content/www/us/en/developer/articles/technical/five-outstanding-additions-sycl2020.html
[l0]: https://spec.oneapi.io/level-zero/latest/index.html
[ocl]: https://www.khronos.org/opencl/
[cuda]: https://developer.nvidia.com/cuda-toolkit
[hip]: https://github.com/ROCm-Developer-Tools/HIP
