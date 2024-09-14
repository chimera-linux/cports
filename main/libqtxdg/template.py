pkgname = "libqtxdg"
pkgver = "4.0.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "lxqt-build-tools",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Qt implementation of freedesktop.org xdg specs"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/libqtxdg"
source = f"{url}/releases/download/{pkgver}/libqtxdg-{pkgver}.tar.xz"
sha256 = "8c1b250de914b2e1fb451c213ee6f249b7b5729c85ac3283fd75615a47a66b62"


@subpackage("libqtxdg-devel")
def _(self):
    return self.default_devel()
