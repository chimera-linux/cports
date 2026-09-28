pkgname = "igsc"
pkgver = "0.9.6"
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
license = "Apache-2.0"
url = "https://github.com/intel/igsc"
source = f"{url}/archive/refs/tags/V{pkgver}.tar.gz"
sha256 = "2c6440cb459ca897dc84e405f32a7e120c9fa0eb9038ea04319cc929ef58ec5c"


@subpackage("igsc-devel")
def _(self):
    return self.default_devel()
