pkgname = "modemmanager-qt"
pkgver = "6.3.0"
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
sha256 = "9cf3029746a8b8b3740bc4de93f138664325c7f4fe8017d92e342e7bc43ec7cf"
hardening = ["vis", "!cfi"]


@subpackage("modemmanager-qt-devel")
def _devel(self):
    self.depends += ["modemmanager-devel"]

    return self.default_devel()
