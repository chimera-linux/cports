pkgname = "modemmanager-qt"
pkgver = "6.2.0"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "modemmanager-devel",
    "qt6-qtbase-devel",
]
checkdepends = [
    "dbus",
]
depends = [
    "modemmanager",
]
pkgdesc = "Qt ModemManager D-Bus API wrapper"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/modemmanager-qt/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/modemmanager-qt-{pkgver}.tar.xz"
sha256 = "f3d1db9ac64a353334b074e45cd07fce4b40ac1388c964f8b269746dc35beea8"
hardening = ["vis", "cfi"]


@subpackage("modemmanager-qt-devel")
def _devel(self):
    self.depends += ["modemmanager-devel"]

    return self.default_devel()
