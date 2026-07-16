pkgname = "knighttime"
pkgver = "6.7.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "kholidays-devel",
    "ki18n-devel",
    "qt6-qtbase-devel",
    "qt6-qtpositioning-devel",
]
pkgdesc = "KDE helpers for scheduling the dark-light cycle"
license = "LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/knighttime"
source = f"$(KDE_SITE)/plasma/{pkgver}/knighttime-{pkgver}.tar.xz"
sha256 = "22295cf3640e15eb04d28350934a1d457a4ec578033af8c28948bd10a8c75387"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("knighttime-devel")
def _(self):
    return self.default_devel()
