pkgname = "bluez-qt"
pkgver = "6.29.0"
pkgrel = 0
build_style = "cmake"
# needs a "real" environment?
make_check_args = [
    "-E",
    "bluezqt-(managertest|adaptertest|mediatest|leadvertisingmanagertest|gattmanagertest|qmltests)",
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "pkgconf"]
makedepends = ["qt6-qtdeclarative-devel", "qt6-qttools-devel"]
checkdepends = ["dbus"]
depends = ["bluez"]
pkgdesc = "Qt wrapper for Bluez 5 D-Bus API"
license = "LGPL-2.1-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/bluez-qt-{pkgver}.tar.xz"
sha256 = "15e2ae85d0e3e205cd17c3c5f079d2263abc4a341fbf223b2561510f69382a2b"
hardening = ["vis"]


@subpackage("bluez-qt-devel")
def _(self):
    self.depends += ["qt6-qtdeclarative-devel"]

    return self.default_devel()
