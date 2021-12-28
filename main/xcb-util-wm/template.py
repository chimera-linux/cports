pkgname = "xcb-util-wm"
pkgver = "0.4.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "bsdm4"]
makedepends = ["xcb-util-devel"]
pkgdesc = "XCB utilities library - window manager helpers for ICCCM"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"{url}/dist/{pkgname}-{pkgver}.tar.bz2"
sha256 = "28bf8179640eaa89276d2b0f1ce4285103d136be6c98262b6151aaee1d3c2a3f"

def post_install(self):
    self.install_license("COPYING")

@subpackage("xcb-util-wm-devel")
def _devel(self):
    return self.default_devel()
