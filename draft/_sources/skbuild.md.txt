# oneAPI Python extensions

DPC++ is a single source compiler. It generates [both the host code and the device code][compilation-flow] in a single fat binary.
DPC++ is an LLVM-based compiler, but it is compatible with GCC runtime libraries. Thus native Python extensions authored in C++ can be
directly built with DPC++.

[compilation-flow]: https://www.intel.com/content/www/us/en/develop/documentation/oneapi-programming-guide/top/programming-interface/compilation-flow-overview.html