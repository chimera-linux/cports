pkgname = "kdbusaddons"
pkgver = "6.19.0"
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
sha256 = "05f4aea54ce8bf9e62ebd48791e9aceba5cbc5aaf195a32ce2497fac2b64aa0d"
hardening = ["vis"]


@subpackage("kdbusaddons-devel")
def _(self):
    return self.default_devel()
