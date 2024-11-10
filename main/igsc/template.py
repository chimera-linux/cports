pkgname = "igsc"
pkgver = "0.9.5"
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
sha256 = "516a099239ad0541598be87025556c878c0d11c6d43e09115d2bb2e24508b6ec"


@subpackage("igsc-devel")
def _(self):
    return self.default_devel()
