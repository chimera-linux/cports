pkgname = "libdbusmenu-lxqt"
pkgver = "0.2.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["qt6-qtbase-devel"]
pkgdesc = "Qt implementation of the DBusMenu spec"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "LGPL-2.0-or-later"
url = "https://github.com/lxqt/libdbusmenu-lxqt"
source = f"{url}/releases/download/{pkgver}/libdbusmenu-lxqt-{pkgver}.tar.xz"
sha256 = "8c22a77c7f69061e5b880cc76ddfc9391b80ee7449485806adecb7123501d84e"


@subpackage("libdbusmenu-lxqt-devel")
def _(self):
    return self.default_devel()
