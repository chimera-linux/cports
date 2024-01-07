pkgname = "libdisplay-info"
pkgver = "0.1.1"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "meson",
    "ninja",
    "pkgconf",
]
makedepends = [
    "hwdata-devel",
]
pkgdesc = "EDID and DisplayID library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://gitlab.freedesktop.org/emersion/libdisplay-info"
source = f"{url}/-/archive/{pkgver}/libdisplay-info-{pkgver}.tar.gz"
sha256 = "a5aeef57817916286526292ec816a5338c4d3c0094ce91e584fc82b57070a44f"
# edid-decode
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libdisplay-info-devel")
def _dev(self):
    return self.default_devel()
