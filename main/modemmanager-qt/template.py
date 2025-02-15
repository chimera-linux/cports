pkgname = "modemmanager-qt"
pkgver = "6.11.0"
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
sha256 = "a636323902c57a9abf199168e9c33b3432c538e276251e6bb7ce753fffef5fee"
hardening = ["vis"]


@subpackage("modemmanager-qt-devel")
def _(self):
    self.depends += ["modemmanager-devel"]

    return self.default_devel()
