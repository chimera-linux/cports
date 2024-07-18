pkgname = "igsc"
pkgver = "0.8.20"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DSYSLOG=OFF", "-DENABLE_WERROR=OFF"]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "linux-headers",
    "metee-devel",
    "udev-devel",
]
pkgdesc = "Intel graphics system controller firmware update library"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/intel/igsc"
source = f"{url}/archive/refs/tags/V{pkgver}.tar.gz"
sha256 = "fb8f36ba532622d58ec48a127da3aa1a282363a3942889a5de47868f0d9fd13e"


@subpackage("igsc-devel")
def _devel(self):
    return self.default_devel()
