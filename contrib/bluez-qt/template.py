pkgname = "bluez-qt"
pkgver = "6.4.0"
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
sha256 = "d2d0aee9f42b501c00711565c2ebe87c608ae4c0786d901386fc55c65039b16b"
hardening = ["vis"]


@subpackage("bluez-qt-devel")
def _devel(self):
    self.depends += ["qt6-qtdeclarative-devel"]

    return self.default_devel()
