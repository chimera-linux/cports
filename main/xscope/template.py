pkgname = "xscope"
pkgver = "1.4.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "xorg-util-macros",
]
makedepends = ["libxt-devel", "xtrans"]
pkgdesc = "Program to monitor X11 Server/Client conversations"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"{url}/archive/individual/app/xscope-{pkgver}.tar.gz"
sha256 = "b9b85fff1c441f8da8831d4d7cc5c8a0f511b2c652a311cc399ba5ebbc8c8939"


def post_install(self):
    self.install_license("COPYING")
