pkgname = "kglobalacceld"
pkgver = "6.7.91"
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
source = f"$(KDE_UNSTABLE_SITE)/plasma/{pkgver}/kglobalacceld-{pkgver}.tar.xz"
sha256 = "1981ba850567d14e8de05fa2c74980e688cd01bb654b5b43e07ccccd0762da3b"
hardening = ["vis"]
options = ["etcfiles"]


@subpackage("kglobalacceld-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel()
