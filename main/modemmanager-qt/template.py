pkgname = "modemmanager-qt"
pkgver = "6.20.0"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "pkgconf"]
makedepends = ["modemmanager-devel", "qt6-qttools-devel"]
checkdepends = ["dbus"]
depends = ["modemmanager"]
pkgdesc = "Qt ModemManager D-Bus API wrapper"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/modemmanager-qt/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/modemmanager-qt-{pkgver}.tar.xz"
sha256 = "1a606b26530de4d9c272cb9793b63b25e80fe7a9c0b61e422399453ff5e5ca79"
hardening = ["vis"]


@subpackage("modemmanager-qt-devel")
def _(self):
    self.depends += ["modemmanager-devel"]

    return self.default_devel()
