pkgname = "xcb-util-keysyms"
pkgver = "0.4.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xcb-util-devel"]
pkgdesc = "XCB utilities library - key constants and keycode conversion"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"{url}/dist/{pkgname}-{pkgver}.tar.gz"
sha256 = "1fa21c0cea3060caee7612b6577c1730da470b88cbdf846fa4e3e0ff78948e54"

@subpackage("xcb-util-keysyms-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
