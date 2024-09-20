pkgname = "xcb-util-keysyms"
pkgver = "0.4.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf", "xorg-util-macros"]
makedepends = ["xcb-util-devel"]
pkgdesc = "XCB utilities library - key constants and keycode conversion"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"{url}/dist/xcb-util-keysyms-{pkgver}.tar.gz"
sha256 = "1fa21c0cea3060caee7612b6577c1730da470b88cbdf846fa4e3e0ff78948e54"


def post_install(self):
    self.install_license("COPYING")


@subpackage("xcb-util-keysyms-devel")
def _(self):
    return self.default_devel()
