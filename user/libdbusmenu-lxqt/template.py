pkgname = "libdbusmenu-lxqt"
pkgver = "0.4.0"
pkgrel = 0
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
sha256 = "b7f94d653559f021932aada76291e933535431a337c39c1a146d0461dd27a103"


@subpackage("libdbusmenu-lxqt-devel")
def _(self):
    return self.default_devel()
