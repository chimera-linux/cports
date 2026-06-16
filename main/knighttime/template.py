pkgname = "knighttime"
pkgver = "6.7.0"
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
sha256 = "c2fc7529cef3b3a80be4715286d027fc8908ef0fe8040aea106831a5265fc113"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("knighttime-devel")
def _(self):
    return self.default_devel()
