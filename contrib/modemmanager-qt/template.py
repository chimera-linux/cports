pkgname = "modemmanager-qt"
pkgver = "6.5.0"
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
sha256 = "76c2b18c9c5c5d9c360282a031feaae966029322f19de050d91d39207cd5717b"
hardening = ["vis"]


@subpackage("modemmanager-qt-devel")
def _(self):
    self.depends += ["modemmanager-devel"]

    return self.default_devel()
