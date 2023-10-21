pkgname = "kguiaddons"
pkgver = "6.2.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "plasma-wayland-protocols",
    "qt6-qtbase-devel",
    "qt6-qtwayland-devel",
]
pkgdesc = "KDE addons to QtGui"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://api.kde.org/frameworks/kguiaddons/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kguiaddons-{pkgver}.tar.xz"
sha256 = "ba5a5e42d5b9b94486419263836074429fd3facfc364fd4e3a29a54bc6de5ddb"
hardening = ["vis", "cfi"]


@subpackage("kguiaddons-devel")
def _devel(self):
    return self.default_devel()
