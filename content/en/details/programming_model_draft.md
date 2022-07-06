---
title: "Programming Model"
date: 2022-07-01
type: docs
toc_hide: true
hide_summary: true
weight: 50
---

The programming model for the **Data Parallel Extensions for Python** (DPX4Py)
suite derives from the oneAPI [programming model][oneAPI-wiki] for device
offload. In oneAPI, a computation kernel can be specified using generic C++
programming and then the kernel can be offloaded to any device that is supported
by an underlying SYCL runtime. The device to which the kernel is offloaded is
specified using an execution queue when *launching* the kernel.

The oneAPI unified programming model brings portability across heterogeneous architectures.
Another important aspect of the programming model is its inherent flexibility
that makes it possible to go beyond portability and even strive for performance
portability. An oneAPI library may be implemented using C++ techniques such as
template metaprogramming or dynamic polymorphism to implement specializations
for a generic kernel. If a kernel is implemented polymorphically, the
specialized implementation will be dispatched based on the execution queue
specified during kernel launch. the oneMKL library is an example of a
performance portable oneAPI library. Figure below shows a **gemv** kernel from the
[oneMKL library][onemkl-gemv] that can be launched on multiple types of architectures
simply by changing the execution queue.

**TODO: Add gemv figure**

In the oneAPI and SYCL programming model, the device where data is allocated is
not tightly coupled with the device where a kernel is executed. The model allows
for implicit data movement across devices. The design offers flexibility to
oneAPI users many of whom are experienced C++ programmers. When extending the
oneAPI programming model to Python via the DPX4Py suite, we felt the need to
make few adjustments to make the model more suited to the Python programming
language. One of the [key Python tenets][pep20] is: *explicit is better than
implicit*. Following the tenet, a *Pythonic* programming model for device
offload should allow a programmer to explicitly answer the following two key
questions: **Where is data allocated?**, **Where would the computation occur?**
Moreover, if data needs to be moved to a device a programmer should have
explicit control of any such data movement. These requirements are fulfilled by
a programming model called *compute follows data*.

### Compute follows data

**TODO:**
* describe compute follows data
* cite Array API
* present example

* End with a rationale. Mention that it does not violate oneAPI programming
  model.

### Extra knobs

**TODO:**

* DPX4Py does support the overall oneAPI programming model. Present current way
  of launching kernels in dpex.
* Compute follows data is the prescribed model, but libraries can support
  implicit data movement (similar to CuPy or TensorFlow) if the want.


[sycl]: https://www.khronos.org/sycl/
[oneAPI-wiki]: https://en.wikipedia.org/wiki/OneAPI_(compute_acceleration)
[pep20]: https://peps.python.org/pep-0020/
[onemkl-gemv]: https://spec.oneapi.io/versions/latest/elements/oneMKL/source/domains/blas/gemv.html#gemv-usm-version
