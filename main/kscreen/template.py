pkgname = "kscreen"
pkgver = "6.7.3"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcmutils-devel",
    "kconfig-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kitemmodels-devel",
    "ksvg-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "layer-shell-qt-devel",
    "libkscreen-devel",
    "libplasma-devel",
    "plasma5support-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtsensors-devel",
    "qt6-qtwayland-devel",
    "wayland-protocols",
    "xcb-util-devel",
]
depends = [
    "kdeclarative",
    "kimageformats",
    "plasma5support",
]
pkgdesc = "KDE screen management"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/kscreen"
source = f"$(KDE_SITE)/plasma/{pkgver}/kscreen-{pkgver}.tar.xz"
sha256 = "dfe6a724dd758d5d9512562f59559944c5c94e1d2a259d0fd61d8eb74439f34c"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
