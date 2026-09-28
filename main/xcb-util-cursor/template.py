pkgname = "xcb-util-cursor"
pkgver = "0.1.6"
pkgrel = 0
build_style = "gnu_configure"
configure_env = {"M4": "/usr/bin/gm4"}
hostmakedepends = [
    "automake",
    "gm4",
    "libtool",
    "pkgconf",
    "xorg-util-macros",
]
makedepends = ["xcb-util-renderutil-devel", "xcb-util-image-devel"]
pkgdesc = "XCB utilities library - port of libxcursor"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"https://xorg.freedesktop.org/archive/individual/lib/xcb-util-cursor-{pkgver}.tar.xz"
sha256 = "fdeb8bd127873519be5cc70dcd0d3b5d33b667877200f9925a59fdcad8f7a933"


def post_install(self):
    self.install_license("COPYING")


@subpackage("xcb-util-cursor-devel")
def _(self):
    return self.default_devel()
