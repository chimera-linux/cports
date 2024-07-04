pkgname = "libdisplay-info"
pkgver = "0.2.0"
pkgrel = 0
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
sha256 = "f7331fcaf5527251b84c8fb84238d06cd2f458422ce950c80e86c72927aa8c2b"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libdisplay-info-devel")
def _devel(self):
    return self.default_devel()
