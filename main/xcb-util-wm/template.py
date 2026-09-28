pkgname = "xcb-util-wm"
pkgver = "0.4.2"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xcb-util-devel"]
pkgdesc = "XCB utilities library - window manager helpers for ICCCM"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"{url}/dist/xcb-util-wm-{pkgver}.tar.gz"
sha256 = "dcecaaa535802fd57c84cceeff50c64efe7f2326bf752e16d2b77945649c8cd7"


def post_install(self):
    self.install_license("COPYING")


@subpackage("xcb-util-wm-devel")
def _(self):
    return self.default_devel()
