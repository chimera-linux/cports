pkgname = "libdbusmenu-lxqt"
pkgver = "0.3.0"
pkgrel = 1
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["qt6-qtbase-devel"]
pkgdesc = "Qt implementation of the DBusMenu spec"
license = "LGPL-2.0-or-later"
url = "https://github.com/lxqt/libdbusmenu-lxqt"
source = f"{url}/releases/download/{pkgver}/libdbusmenu-lxqt-{pkgver}.tar.xz"
sha256 = "ada0d14d3a4d9fb0ba344bf078d351046dfd226da1096f866d78167a79243ff9"


@subpackage("libdbusmenu-lxqt-devel")
def _(self):
    return self.default_devel()
