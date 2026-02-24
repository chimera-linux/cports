pkgname = "plasma-activities-stats"
pkgver = "6.6.0"
pkgrel = 1
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "plasma-activities-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["dbus", "kactivitymanagerd"]
pkgdesc = "Library to access KDE activity manager statistics data"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/plasma/plasma-activities-stats"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-activities-stats-{pkgver}.tar.xz"
sha256 = "03fe7bda7db2dd30cb26cbb87d2829965532439a8d6532be089e317629ea9b5a"
hardening = ["vis"]


@subpackage("plasma-activities-stats-devel")
def _(self):
    return self.default_devel()
