pkgname = "networkmanager-qt"
pkgver = "6.13.0"
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
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/networkmanager-qt/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/networkmanager-qt-{pkgver}.tar.xz"
sha256 = "9a9e3595a1b9816b2737b0416b9d92b76e2b0ca0989d0ef65a95e5f895ac36c1"
hardening = ["vis"]


@subpackage("networkmanager-qt-devel")
def _(self):
    self.depends += ["networkmanager-devel"]

    return self.default_devel()
