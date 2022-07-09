---
title: "Features Summary"
date: 2022-07-08
type: docs
weight: 30
description: >
  A list of the main features of the data-parallel extensions to Python packages.
---

## Cross-platform Native Extensions

DPC++ lets you build cross-platform libraries that can be run on a growing set
of heterogeneous devices supported by the compiler, such as Intel CPUs, GPUs,
and FPGAs, and also Nvidia GPUs and AMD GPUs.

Our package [dpctl][dpctl] provides the necessary Python bindings to make a SYCL
library into a Python native extension and subsequently use it from Python.

## Write Kernels Directly in Python

If C++ is not your language, you can skip writing data-parallel kernels in SYCL
and directly write them in Python.

Our package [numba-dpex][numba-dpex] extends the Numba compiler to allow kernel
creation directly in Python via a custom compute API.

## Cross-architecture Array API

Python array library targeting conformance to core [Python Array API][array-api]
specification.

[dpctl.tensor][tensor] is a Python native extension library implemented using
SYCL within [dptcl][dpctl]. The library lets Python users get their job done
using tensor operations powered by pure SYCL generic kernels for portability.

## Easy to Install

All the data-parallel extensions for Python packages are readily available for
installation on conda, PyPI, or github.

oneAPI Intel LLVM compilers, including DPC++, as well as associated runtimes are
available on conda to support present and future data-parallel extensions.


[dpctl]: https://intelpython.github.io/dpctl/latest/index.html
[numba-dpex]: https://intelpython.github.io/numba-dpex/latest/index.html
[array-api]: https://data-apis.org/array-api/latest/
[tensor]: https://intelpython.github.io/dpctl/latest/docfiles/dpctl/dpctl.tensor_pyapi.html#dpctl-tensor-pyapi
