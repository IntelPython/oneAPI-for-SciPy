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
   2. How does a Python application manage data sharing?
   3. How does a Python workload specify computations to be offloaded to selected devices?

Python package `dpctl` answers these questions. All the computational devices known to the 
underlying DPC++ runtime can be accessed using `dpctl.get_devices()`. A specific device of 
interest [can be selected][device_selection] either using a helper function, 
e.g. `dpctl.select_gpu_device()`,  or by passing a filter selector string to `dpctl.SyclDevice` constructor.

[device_selection]: https://intelpython.github.io/dpctl/latest/docfiles/user_guides/manual/dpctl/device_selection.html