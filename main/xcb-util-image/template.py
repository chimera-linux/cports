pkgname = "xcb-util-image"
pkgver = "0.4.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xcb-util-devel"]
pkgdesc = "XCB utilities library - XImage and XShmImage"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"{url}/dist/xcb-util-image-{pkgver}.tar.gz"
sha256 = "0ebd4cf809043fdeb4f980d58cdcf2b527035018924f8c14da76d1c81001293b"


def post_install(self):
    self.install_license("COPYING")


@subpackage("xcb-util-image-devel")
def _(self):
    return self.default_devel()
