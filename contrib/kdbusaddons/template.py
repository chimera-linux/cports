pkgname = "kdbusaddons"
pkgver = "6.2.0"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
checkdepends = [
    "dbus",
]
pkgdesc = "KDE Widgets for configuration dialogs"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://api.kde.org/frameworks/kdbusaddons/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kdbusaddons-{pkgver}.tar.xz"
sha256 = "bca0df3fc7361effcf81ffb795d8ff62e2189ea9672492d6b26c1e0144fedd67"
hardening = ["vis", "cfi"]


@subpackage("kdbusaddons-devel")
def _devel(self):
    return self.default_devel()
