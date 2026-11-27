pkgname = "libdbusmenu-lxqt"
pkgver = "0.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "lxqt-build-tools",
    "ninja",
    "pkgconf",
]
makedepends = ["qt6-qtbase-devel"]
pkgdesc = "Qt implementation of the DBusMenu spec"
license = "LGPL-2.0-or-later"
url = "https://github.com/lxqt/libdbusmenu-lxqt"
source = f"{url}/releases/download/{pkgver}/libdbusmenu-lxqt-{pkgver}.tar.xz"
sha256 = "64083c3cd606bda18adb50d5e8bbdec79fffdd2df485b153037d8e235ae33390"


@split("devel")
def _(self):
    return self.default_devel()
