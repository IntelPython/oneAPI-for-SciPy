---
title: "Install Intel(R) oneAPI toolkits"
date: 2022-06-14
type: docs
weight: 30
description: >
  Pointers about how to get Intel(R) oneAPI toolkits.
---

# Installation of Intel(R) oneAPI toolkits

## Use Intel(R) DevCloud

[Get free access][intel-devcloud] to a development sandbox with preinstalled and configured
oneAPI toolkits as well as access variety of Intel hardware. This is great and low effort way
to start exploring oneAPI. We recommend to start with [Jupyter Lab][dev-cloud-jupyter-lab].

## Install locally

To add oneAPI to your local toolbox, download and install the basekit for your operating system from [download page][get-basekit].

{{< alert title="Note" >}}
For Linux*, toolkits can be installed using OS's package managers, as well as tried out from within a docker-container. Please refer
to the download page for specifics.
{{< /alert >}}

Make sure to configure your system by following steps from "[Get Started Guide][get-started]"
document applicable for your operating system.

## Install in CI

oneAPI can be installed into Linux-powered CI by using the OS's package manager and installing
only the necessary components from required toolkits.

See [this example][install-dpcpp-in-github] of installing DPC++ compiler in GitHub actions
for [IntelPython/dpctl][dpctl] project.


[intel-devcloud]: https://devcloud.intel.com/oneapi/
[dev-cloud-jupyter-lab]: https://jupyter.oneapi.devcloud.intel.com/hub/login?next=/lab/tree/Welcome.ipynb?reset
[get-basekit]: https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit-download.html
[get-started]: https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html#gs.3mwueb
[install-dpcpp-in-github]: https://github.com/IntelPython/dpctl/blob/1f8e4b35c3d623bd7e0d84dad32f421aef34ac0f/.github/workflows/generate-docs.yml#L18-L29
[dpctl]: https://github.com/IntelPython/dpctl
