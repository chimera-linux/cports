pkgname = "libfm-qt"
pkgver = "2.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "lxqt-build-tools", "ninja", "perl", "pkgconf"]
makedepends = [
    "libexif-devel",
    "lxqt-menu-data",
    "qt6-qtbase-devel",
    "qt6-qtbase-private-devel",
    "qt6-qttools-devel",
]
depends = ["lxqt-menu-data"]
pkgdesc = "Qt binding for libfm"
license = "LGPL-2.0-or-later"
url = "https://github.com/lxqt/libfm-qt"
source = f"{url}/releases/download/{pkgver}/libfm-qt-{pkgver}.tar.xz"
sha256 = "866204267d6d0e66c8abe0f14e874cad41645ad92b90660b428c8e4dd64722af"


@split("devel")
def _(self):
    return self.default_devel()
