pkgname = "xcb-util-image"
pkgver = "0.4.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xcb-util-devel"]
pkgdesc = "XCB utilities library - XImage and XShmImage"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"{url}/dist/{pkgname}-{pkgver}.tar.bz2"
sha256 = "2db96a37d78831d643538dd1b595d7d712e04bdccf8896a5e18ce0f398ea2ffc"

def post_install(self):
    self.install_license("COPYING")

@subpackage("xcb-util-image-static")
def _static(self):
    return self.default_static()

@subpackage("xcb-util-image-devel")
def _devel(self):
    return self.default_devel(man = True)
