pkgname = "kdecoration"
pkgver = "6.7.91"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "ki18n-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE Plugin based library to create window decorations"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://kde.org/plasma-desktop"
source = f"$(KDE_UNSTABLE_SITE)/plasma/{pkgver}/kdecoration-{pkgver}.tar.xz"
sha256 = "ad5a5d40635e577b4a72e4797f67a7a0a2b42bcaa28110b0f3606d8d5fe323fa"
hardening = ["vis"]


@subpackage("kdecoration-devel")
def _(self):
    return self.default_devel()
