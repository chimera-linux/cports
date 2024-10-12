pkgname = "xscope"
pkgver = "1.4.4"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "xorg-util-macros",
]
makedepends = ["libxt-devel", "xtrans"]
pkgdesc = "Program to monitor X11 Server/Client conversations"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"{url}/archive/individual/app/xscope-{pkgver}.tar.gz"
sha256 = "4d1d538fc7b32a25eda3570abdb94c145dd1adfd900bda1d33654c83c96dbb9d"


def post_install(self):
    self.install_license("COPYING")
