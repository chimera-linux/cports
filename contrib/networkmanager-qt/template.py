pkgname = "networkmanager-qt"
pkgver = "6.2.0"
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
sha256 = "7be22a6bbc5843b1ada0a170fb56c9c96bef643d7d485413f2af792914ed02d2"
hardening = ["vis", "cfi"]


@subpackage("networkmanager-qt-devel")
def _devel(self):
    self.depends += ["networkmanager-devel"]

    return self.default_devel()
