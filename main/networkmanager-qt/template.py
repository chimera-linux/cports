pkgname = "networkmanager-qt"
pkgver = "6.6.0"
pkgrel = 0
build_style = "cmake"
# parallel causes {settings,activeconnection}test to be flaky
make_check_args = ["-j1"]
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "networkmanager-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = [
    "dbus",
]
depends = [
    "networkmanager",
]
pkgdesc = "Qt NetworkManager D-Bus API wrapper"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/networkmanager-qt/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/networkmanager-qt-{pkgver}.tar.xz"
sha256 = "06392d71e6e09758cb1b433d3b1dc667cb59dd7a96b3510f232b5cadff332e40"
hardening = ["vis"]


@subpackage("networkmanager-qt-devel")
def _(self):
    self.depends += ["networkmanager-devel"]

    return self.default_devel()
