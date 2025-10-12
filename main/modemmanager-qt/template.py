pkgname = "modemmanager-qt"
pkgver = "6.19.0"
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
sha256 = "367148c7f7c4ec8923cafcba4ad0dc500434c95db963755704a2521cc6c2f0d0"
hardening = ["vis"]


@subpackage("modemmanager-qt-devel")
def _(self):
    self.depends += ["modemmanager-devel"]

    return self.default_devel()
