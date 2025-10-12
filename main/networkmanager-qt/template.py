pkgname = "networkmanager-qt"
pkgver = "6.19.0"
pkgrel = 0
build_style = "cmake"
# parallel causes {settings,activeconnection}test to be flaky
make_check_args = ["-j1"]
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "pkgconf"]
makedepends = [
    "networkmanager-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
checkdepends = ["dbus"]
depends = ["networkmanager"]
pkgdesc = "Qt NetworkManager D-Bus API wrapper"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/networkmanager-qt/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/networkmanager-qt-{pkgver}.tar.xz"
sha256 = "83ba1060080dc193c62837421e1cb796500abb3931b505ae8275c440674affc4"
hardening = ["vis"]


@subpackage("networkmanager-qt-devel")
def _(self):
    self.depends += ["networkmanager-devel"]

    return self.default_devel()
