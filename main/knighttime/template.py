pkgname = "knighttime"
pkgver = "6.6.1"
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
sha256 = "e3a65155d7bd2d71309c1e54e9047f15eb407030e1bd4db913406b8c59863d39"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("knighttime-devel")
def _(self):
    return self.default_devel()
