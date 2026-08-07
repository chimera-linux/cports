pkgname = "libqtxdg"
pkgver = "4.4.0"
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
sha256 = "34d25949ae7b6275fb54da46187dd8ba41771600353405b15e53bdc90b9e287a"
options = ["etcfiles"]


@subpackage("libqtxdg-devel")
def _(self):
    return self.default_devel()
