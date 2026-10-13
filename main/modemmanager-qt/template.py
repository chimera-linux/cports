pkgname = "modemmanager-qt"
pkgver = "6.31.0"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "pkgconf"]
makedepends = ["modemmanager-devel", "qt6-qttools-devel"]
checkdepends = ["dbus"]
depends = ["modemmanager"]
pkgdesc = "Qt ModemManager D-Bus API wrapper"
license = "LGPL-2.1-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/modemmanager-qt-{pkgver}.tar.xz"
sha256 = "e816565ce4b915fa885a6b039e582a477e84bb01bca3229df5f1b79dfa01b810"
hardening = ["vis"]


@subpackage("modemmanager-qt-devel")
def _(self):
    self.depends += ["modemmanager-devel"]

    return self.default_devel()
