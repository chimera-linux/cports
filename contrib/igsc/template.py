pkgname = "igsc"
pkgver = "0.8.18"
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
sha256 = "8c6460ac3dedf7f12b4a278bead9043f56fa8a7309425a4eb97a6a2245d1b74d"


@subpackage("igsc-devel")
def _devel(self):
    return self.default_devel()
