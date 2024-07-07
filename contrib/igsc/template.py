pkgname = "igsc"
pkgver = "0.8.16"
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
sha256 = "03e797f23f48221ce797227a1059edd7bceade189966cc1550f4c1d64dbc1550"


@subpackage("igsc-devel")
def _devel(self):
    return self.default_devel()
