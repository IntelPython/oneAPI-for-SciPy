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

### Building first extension

```bash
CXX=dpcpp LDSHARED="dpcpp --shared" python setup.py develop
```

[dpcpp-single-source]: https://oneapi-src.github.io/DPCPP_Reference/#data-parallel-c-dpc
[compilation-flow]: https://www.intel.com/content/www/us/en/develop/documentation/oneapi-programming-guide/top/programming-interface/compilation-flow-overview.html
[intel-llvm]: https://github.com/intel/llvm.git
[intel-llvm-getting-started]: https://github.com/intel/llvm/blob/sycl/sycl/doc/GetStartedGuide.md
