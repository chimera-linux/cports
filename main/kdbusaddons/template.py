pkgname = "kdbusaddons"
pkgver = "6.6.0"
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
sha256 = "521315f80d31e2db4e4344ebf2436a22e75475b70edabe8157f4afb4a2cb42ad"
hardening = ["vis"]


@subpackage("kdbusaddons-devel")
def _(self):
    return self.default_devel()
