---
title: About authors
linkTitle: About
type: docs
layout: docs
menu:
  main:
    weight: 10

---

This poster is being presented on behalf of [Python team](https://github.com/IntelPython) at [Intel Corporation](http://www.intel.com).

Our mission is to foster adoption of oneAPI program by Python community at large and 
Scientific Python community in particular.

To this end, we are developing the following Python packages:

  - [github.com/IntelPython/dpctl][dpctl]
     - Python bindings to DPC++ runtime classes
     - support for device selection, sub-device creation, USM memory allocations, context/queue creation
     - [array API][array-api] implementation using DPC++
     - integration with [Cython][cython] and [pybind11][pybind11] to facilitate building of oneAPI Python extensions
     - small footprint
  - [github.com/IntelPython/dpnp][dpnp]
     - oneAPI- and oneMKL-powered implementation for array library with NumPy-compatible API
  - [github.com/IntelPython/numba-dpex][dpex]
     - Numba extension to compile Python functions for Intel(R) XPUs

[dpctl]: https://github.com/IntelPython/dpctl.git
[cython]: https://github.com/cython/cython.git
[pybind11]: https://github.com/pybind/pybind11.git
[dpnp]: https://github.com/IntelPython/dpnp.git
[dpex]: https://github.com/IntelPython/numba-dpex.git
[array-api]: https://data-apis.org/array-api/latest/