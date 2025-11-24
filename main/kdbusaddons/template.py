pkgname = "kdbusaddons"
pkgver = "6.20.0"
pkgrel = 1
build_style = "cmake"
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qttools-devel",
]
checkdepends = [
    "dbus",
]
pkgdesc = "KDE Widgets for configuration dialogs"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://api.kde.org/frameworks/kdbusaddons/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kdbusaddons-{pkgver}.tar.xz"
sha256 = "5db2f6b7235238070224ee8a5225f41ffdb3249d558a81a7c06a8e54d67729f7"
hardening = ["vis"]


@subpackage("kdbusaddons-devel")
def _(self):
    return self.default_devel()
