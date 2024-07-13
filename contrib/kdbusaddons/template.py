pkgname = "kdbusaddons"
pkgver = "6.4.0"
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
sha256 = "212fa6be4194a819f0fb48f3c6fd2b58846ba911612b73e97dc7e90f6104c987"
hardening = ["vis", "!cfi"]


@subpackage("kdbusaddons-devel")
def _devel(self):
    return self.default_devel()
