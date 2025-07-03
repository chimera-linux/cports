pkgname = "plasma5support"
pkgver = "6.4.2"
pkgrel = 0
build_style = "cmake"
# needs plasma-workspace plugin and is circular with it
make_check_args = ["-E", "pluginloadertest"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kidletime-devel",
    "kio-devel",
    "knotifications-devel",
    "kservice-devel",
    "libksysguard-devel",
    "networkmanager-qt-devel",
    "plasma-activities-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
    "solid-devel",
]
# some qt5 compat modules were moved here ~6.1.0
# also locale file conflicts ~6.2.3 & more plasma-workspace dataengines ~6.3.0
replaces = ["plasma-workspace<6.3.0"]
pkgdesc = "KDE Support components for porting from Qt5/KF5 to Qt6/KF6"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/plasma5support"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma5support-{pkgver}.tar.xz"
sha256 = "24a07ceff083a6a7a2d9b4152812549050623c434ef7319109963085a114aef2"
hardening = ["vis"]


@subpackage("plasma5support-devel")
def _(self):
    self.depends += ["kcoreaddons-devel", "kservice-devel"]

    return self.default_devel()
