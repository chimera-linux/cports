pkgname = "bluez-qt"
pkgver = "6.12.0"
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
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/bluez-qt/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/bluez-qt-{pkgver}.tar.xz"
sha256 = "d8a84cd33a1345301487391c6dc625e277b5a2544d7360e5f6eda02a34cc7558"
hardening = ["vis"]


@subpackage("bluez-qt-devel")
def _(self):
    self.depends += ["qt6-qtdeclarative-devel"]

    return self.default_devel()
