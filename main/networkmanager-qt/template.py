pkgname = "networkmanager-qt"
pkgver = "6.29.0"
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
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/networkmanager-qt-{pkgver}.tar.xz"
sha256 = "23f2736fb8f3f0a3ee2f2f1944720206a4d5c532cf7a0a00c8f73aa69d75f588"
hardening = ["vis"]


@subpackage("networkmanager-qt-devel")
def _(self):
    self.depends += ["networkmanager-devel"]

    return self.default_devel()
