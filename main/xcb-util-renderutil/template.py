pkgname = "xcb-util-renderutil"
pkgver = "0.3.10"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xcb-util-devel"]
pkgdesc = "XCB utilities library - Render extension convenience functions"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"{url}/dist/xcb-util-renderutil-{pkgver}.tar.gz"
sha256 = "e04143c48e1644c5e074243fa293d88f99005b3c50d1d54358954404e635128a"


def post_install(self):
    self.install_license("COPYING")


@subpackage("xcb-util-renderutil-devel")
def _(self):
    return self.default_devel()
