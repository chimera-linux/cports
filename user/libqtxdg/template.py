pkgname = "libqtxdg"
pkgver = "4.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "lxqt-build-tools",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtbase-private-devel",  # qicon_p.h
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Qt implementation of freedesktop.org xdg specs"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/libqtxdg"
source = f"{url}/releases/download/{pkgver}/libqtxdg-{pkgver}.tar.xz"
sha256 = "64edfa2bc219366be099ed37115be9a440f53800974cbc967bca0f7080bca1e5"
options = ["etcfiles"]


@split("devel")
def _(self):
    return self.default_devel()
