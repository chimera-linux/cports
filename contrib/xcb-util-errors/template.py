pkgname = "xcb-util-errors"
pkgver = "1.0.1"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "xorg-util-macros",
]
makedepends = ["libxcb-devel"]
pkgdesc = "XCB errors library"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"{url}/dist/xcb-util-errors-{pkgver}.tar.gz"
sha256 = "cfbd3b022bdb27a6921a4abd6b41f4071b4e4960447598abd30955d3454f4d99"


def post_install(self):
    self.install_license("COPYING")


@subpackage("xcb-util-errors-devel")
def _(self):
    return self.default_devel()
