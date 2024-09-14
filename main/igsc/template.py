pkgname = "igsc"
pkgver = "0.9.3"
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
sha256 = "e657553ebe3dbb7196012bd9a234382f9053522c377651400268ce45b2a9e43a"


@subpackage("igsc-devel")
def _(self):
    return self.default_devel()
