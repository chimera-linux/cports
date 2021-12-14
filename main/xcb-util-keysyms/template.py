pkgname = "xcb-util-keysyms"
pkgver = "0.4.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xcb-util-devel"]
pkgdesc = "XCB utilities library - key constants and keycode conversion"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"{url}/dist/{pkgname}-{pkgver}.tar.bz2"
sha256 = "0ef8490ff1dede52b7de533158547f8b454b241aa3e4dcca369507f66f216dd9"

@subpackage("xcb-util-keysyms-static")
def _static(self):
    return self.default_static()

@subpackage("xcb-util-keysyms-devel")
def _devel(self):
    return self.default_devel(man = True)
