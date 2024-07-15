pkgname = "modemmanager-qt"
pkgver = "6.4.0"
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
sha256 = "f2bc2aa916bce3ea58c38def984c35fada25e8756add400131782bfc62deee9d"
hardening = ["vis"]


@subpackage("modemmanager-qt-devel")
def _devel(self):
    self.depends += ["modemmanager-devel"]

    return self.default_devel()
