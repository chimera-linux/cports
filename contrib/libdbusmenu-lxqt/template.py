pkgname = "libdbusmenu-lxqt"
pkgver = "0.1.0"
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
sha256 = "a82d77375034b0f27e6e08b5c7ad9c19ee88e8d7bb699ee0423a5a0e781fb291"


@subpackage("libdbusmenu-lxqt-devel")
def _(self):
    return self.default_devel()
