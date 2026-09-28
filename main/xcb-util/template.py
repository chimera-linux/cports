pkgname = "xcb-util"
pkgver = "0.4.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gperf",
    "pkgconf",
    "slibtool",
    "xorg-util-macros",
]
makedepends = ["libxcb-devel"]
pkgdesc = "XCB utilities library"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"{url}/dist/xcb-util-{pkgver}.tar.gz"
sha256 = "21c6e720162858f15fe686cef833cf96a3e2a79875f84007d76f6d00417f593a"


def post_install(self):
    self.install_license("COPYING")


@subpackage("xcb-util-devel")
def _(self):
    return self.default_devel()
