---
title: "Quickstart"
date: 2022-06-14
type: docs
weight: 10
description: >
  Get started with oneAPI Python-extensions
---

In a heterogeneous system there may be **multiple** devices a Python user may want to engage.
For example, it is common for a consumer-grade laptop to feature an integrated or a discrete
GPU alongside a CPU.

To harness their power one needs to know how to answer the following 3 key questions:

   1. How does a Python program recognize available computational devices?
   2. How does a Python workload specify computations to be offloaded to selected devices?
   3. How does a Python application manage data sharing?

### Recognizing available devices

Python package `dpctl` answers these questions. All the computational devices known to the 
underlying DPC++ runtime can be accessed using `dpctl.get_devices()`. A specific device of 
interest [can be selected][device_selection] either using a helper function, 
e.g. `dpctl.select_gpu_device()`,  or by passing a filter selector string 
to `dpctl.SyclDevice` constructor.


```python
import dpctl

# select a GPU device. If multiple devices present, 
# let the underlying runtime select from GPUs
dev_gpu = dpctl.SyclDevice("gpu")
# select a CPU device
dev_cpu = dpctl.SyclDevice("cpu")

# stand-alone function, equivalent to C++ 
#   `auto dev = sycl::gpu_selector().select_device();`
dev_gpu_alt = dpctl.select_gpu_device()
# stand-alone function, equivalent to C++ 
#   `auto dev = sycl::cpu_selector().select_device();`
dev_cpu_alt = dpctl.select_cpu_device()
```

A [device object][device] can be used to query properies of the device, such as its name, vendor, maximal number of computational units, memory size, etc.

### Specifying offload target

To answer the second question on the list we need a digression to explain offloading in DPC++ first. A computational task is offloaded for execution on a device
by submitting it to DPC++ runtime which inserts the task in a computational graph. Once the device becomes available the runtime selects a task whose dependencies 
are met for execution. 

The computational graph along with the device targeted by its tasks are stored in a [SYCL queue][queue] object. The task submission is therefore always
associated with a queue. 

Queues can be constructed directly from a device object, or by using a filter selector string to indicate the device to construct:

```python
# construct queue from device object
q1 = dpctl.SyclQueue(dev_gpu)
# construct queue using filter selector
q2 = dpctl.SyclQueue("gpu")
```

The computational tasks can be stored in an oneAPI native extension in which case their submission is orchestrated 
during Python API calls. Let's consider a function that offloads an evaluation of a polynomial for every point of a
NumPy array `X`. Such a function needs to receive a queue object to indicate which device the computation must be 
offloaded too:

```python
# allocate space for the result
Y = np.empty_like(X)
# evaluate polynomial on the device targeted by the queue, Y[i] = p(X[i])
onapi_ext.offloaded_poly_evaluate(q, X, Y)
```

Python call to `onapi_ext.offloaded_poly_evaluate` of NumPy arrays of double precision floating pointer numbers gets 
translated to the following sample C++ code:

```c++
void 
cpp_offloaded_poly_evaluate(
  sycl::queue q, const double *X, double *Y, size_t n) {    
    // create buffers from malloc allocations to make data accessible from device
    sycl::buffer<1, double> buf_X(X, n);
    sycl::buffer<1, double> buf_Y(Y, n);

    q.submit([&](sycl::handler &cgh) {
        // create buffer accessors indicating kernel data-flow pattern  
        sycl::accessor acc_X(buf_X, cgh, sycl::read_only);
        sycl::accessor acc_Y(buf_Y, cgh, sycl::write_only, sycl::no_init);

        cgh.parallel_for(n,
           // lambda function that gets executed by different work-items with 
           // different arguments in parallel
           [=](sycl::id<1> id) {
              auto x = accX[id];
              accY[id] = 3.0 + x * (1.0 + x * (-0.5 + 0.3 * x));
           });
    }).wait();

    return;
}
```

We refer the reader to excellent freely available "[Data Parallel C++][dpcpp-book]" book for details of this C++ snippet.

Our package `numba_dpex` allows one to write kernels in Python as well.

```python
import numba_dpex

@numba_dpex.kernel
def numba_dpex_poly(X, Y):
    i = numba_dpex.get_global_id(0)
    x = X[i]
    Y[i] = 3.0 + x * (1.0 + x * (-0.5 + 0.3 * x))
```

Specifying the execution queue is done using Python context manager:

```python
import numpy as np

X = np.random.randn(10**6)
Y = np.empty_like(X)

with dpctl.device_context(q):
    # apply the kernel to elements of X, writing value into Y, 
    # while executing using given queue
    numba_dpex_poly[X.size, numba_dpex.DEFAULT_LOCAL_SIZE](X, Y)
```

The argument to `device_context` can be a queue object, a device object for which a temporary queue will be created, 
or a filter selector string. Thus we could have equally used `dpctl.device_context(gpu_dev)` or `dpctl.device_context("gpu")`.

Note that in this examples data sharing was implicitly managed for us: in the case of calling a function from a precompiled 
oneAPI native extension data sharing was managed by DPC++ runtime, while in the case of using `numba_dpex` kernel it was managed 
during execution of `__call__` method. 
 
### Data sharing

Implicit data managing is surely convenient, but its use in interpreted code comes at a performance cost. A runtime must 
implicitly copy data from host to the device before the kernel execution commences and then copy some (or all) of it back 
after the execution completes.

`dpctl` provides for allocating memory directly accessible to kernels executing on a device using SYCL's 
Unified Shared Memory ([USM][sycl2020-usm]) feature as well as for the [array-API][array-api] conforming ND-array 
object `dpctl.tensor.usm_ndarray`.

```python
import dpctl.tensor as dpt

# allocate array of doubles using USM-device allocation on GPU device
X = dpt.arange(0., end=1.0, step=1e-6, device="gpu", usm_type="device")
# allocate array for the output
Y = dpt.empty_like(X)

# execution queue is inferred from allocation queues.
# Kernel is executed on the same device where arrays were allocated
numba_dpex_poly[X.size, numba_dpex.DEFAULT_LOCAL_SIZE](X, Y)
```

The execution queue can be unambiguously determined in this case because both arguments are 
USM arrays with the same allocation queues because `X.sycl_queue == Y.sycl_queue` evaluates to `True`. 
Should the queues be different, such an inference becomes impossible and `numba_dpex` raises 
`IndeterminateExecutionQueueError` advising user to explicitly migrate the data.

Migration can be accomplished either by using `dpctl.tensor.asarray(X, device=target_device)`
to create a copy, or by using `X.to_device(target_device)` method.

The result USM array can be copied back into a NumPy array using `dpt.asnumpy(Y)` if needed. 

`dpctl` and `numba_dpex` are both under heavy development. Feel free to file an issue on GitHub or 
reach out on Gitter should you encounter any issues.


[device_selection]: https://intelpython.github.io/dpctl/latest/docfiles/user_guides/manual/dpctl/device_selection.html
[device]: https://intelpython.github.io/dpctl/latest/docfiles/user_guides/manual/dpctl/devices.html
[queue]: https://intelpython.github.io/dpctl/latest/docfiles/user_guides/manual/dpctl/queues.html
[dpcpp-book]: https://link.springer.com/book/10.1007%2F978-1-4842-5574-2
[sycl2020-usm]: https://www.khronos.org/registry/SYCL/specs/sycl-2020/html/sycl-2020.html#sec:usm
[array-api]: https://data-apis.org/array-api/latest/