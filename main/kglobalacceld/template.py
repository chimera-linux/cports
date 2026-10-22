pkgname = "kglobalacceld"
pkgver = "6.8.1"
pkgrel = 0
build_style = "cmake"
# needs full init of kglobalaccel
# migrateconfigtest passes at times but flaky
make_check_args = ["-E", "(migrateconfigtest|shortcutstest)"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kglobalaccel-devel",
    "kio-devel",
    "kservice-devel",
    "kwindowsystem-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
]
checkdepends = ["dbus"]
pkgdesc = "KDE Daemon for global keyboard shortcut functionality"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/kglobalacceld"
source = f"$(KDE_SITE)/plasma/{pkgver}/kglobalacceld-{pkgver}.tar.xz"
sha256 = "33ca06aefb17ee663282fe60a6d2d7211d5832515d1f0a4387a77858bdadf219"
hardening = ["vis"]
options = ["etcfiles"]


@subpackage("kglobalacceld-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel()
