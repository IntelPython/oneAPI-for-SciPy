# Installing Intel(R) oneAPI toolkits

## Use Intel(R) DevCloud

[Get a free access][intel-devcloud] to a development sandbox with preinstalled and configured
oneAPI toolkits and access to a variety of Intel hardware. This is great and low effort way
to start exploring oneAPI.

## Install locally

Download and install the basekit from [download page][get-basekit] for your operating system.

```{note}
For Linux*, toolkits can be installed using OS's package managers, as well as tried out from within a docker-container.
```

Make sure to configure your system by following steps from "[Get Started Guide][get-started]"
document for your operating system.

## Install in CI

oneAPI can be installed into Linux-powered CI by using the OS's package manager and installing
only the necessary components from required toolkits.
See [this example][install-dpcpp-in-github] of installing DPC++ compiler in GitHub actions
for [IntelPython/dpctl][dpctl] project.


[intel-devcloud]: https://devcloud.intel.com/oneapi/
[get-basekit]: https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit-download.html
[get-started]: https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html#gs.3mwueb
[install-dpcpp-in-github]: https://github.com/IntelPython/dpctl/blob/1f8e4b35c3d623bd7e0d84dad32f421aef34ac0f/.github/workflows/generate-docs.yml#L18-L29
[dpctl]: https://github.com/IntelPython/dpctl