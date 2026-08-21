pkgname = "modemmanager-qt"
pkgver = "6.29.0"
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
sha256 = "4af60497e5331b41a3b34e194c1fb4293cd5eae7b50b5ecf5959a9718b223b47"
hardening = ["vis"]


@subpackage("modemmanager-qt-devel")
def _(self):
    self.depends += ["modemmanager-devel"]

    return self.default_devel()
