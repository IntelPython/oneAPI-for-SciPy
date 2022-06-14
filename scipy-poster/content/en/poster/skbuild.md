---
title: "oneAPI Python extensions"
date: 2022-06-14
weight: 2
description: >
  Python extensions can be built with DPC++. This is how.
---

# oneAPI Python extensions

DPC++ is a single source compiler. It generates [both the host code and the device code][compilation-flow] in a single fat binary.
DPC++ is an LLVM-based compiler, but the host portion of the binary it produces is compatible with GCC runtime libraries on Linux and Windows runtime libraries on Windows. Thus native Python extensions authored in C++ can be directly built with DPC++.

[compilation-flow]: https://www.intel.com/content/www/us/en/develop/documentation/oneapi-programming-guide/top/programming-interface/compilation-flow-overview.html