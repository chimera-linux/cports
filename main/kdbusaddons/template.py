pkgname = "kdbusaddons"
pkgver = "6.13.0"
pkgrel = 0
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
sha256 = "9b2f16045a38b0db14d1946a3df552aed45edac981e5bff69fc9752abcb17f9e"
hardening = ["vis"]


@subpackage("kdbusaddons-devel")
def _(self):
    return self.default_devel()
