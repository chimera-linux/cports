pkgname = "xcb-util-cursor"
pkgver = "0.1.5"
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
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"https://xorg.freedesktop.org/archive/individual/lib/xcb-util-cursor-{pkgver}.tar.xz"
sha256 = "0caf99b0d60970f81ce41c7ba694e5eaaf833227bb2cbcdb2f6dc9666a663c57"


def post_install(self):
    self.install_license("COPYING")


@subpackage("xcb-util-cursor-devel")
def _devel(self):
    return self.default_devel()
