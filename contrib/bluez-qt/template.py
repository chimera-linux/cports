pkgname = "bluez-qt"
pkgver = "6.3.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtdeclarative-devel",
]
checkdepends = [
    "dbus",
]
depends = [
    "bluez",
]
pkgdesc = "Qt wrapper for Bluez 5 D-Bus API"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/bluez-qt/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/bluez-qt-{pkgver}.tar.xz"
sha256 = "3b68b83fae1032d84213692b0c908f0fd57cafe57175c62b6ce5b89bc1d4a2dc"
# FIXME: cfi breaks at least almost every test
hardening = ["vis", "!cfi"]


@subpackage("bluez-qt-devel")
def _devel(self):
    self.depends += ["qt6-qtdeclarative-devel"]

    return self.default_devel()
