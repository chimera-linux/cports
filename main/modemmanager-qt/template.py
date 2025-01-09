pkgname = "modemmanager-qt"
pkgver = "6.9.0"
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
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/modemmanager-qt-{pkgver}.tar.xz"
sha256 = "dfd0600d9c93fed229ed9e004cca00180cfff0ed10c1bfd4eb24d889c2f1d056"
hardening = ["vis"]


@subpackage("modemmanager-qt-devel")
def _(self):
    self.depends += ["modemmanager-devel"]

    return self.default_devel()
