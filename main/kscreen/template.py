pkgname = "kscreen"
pkgver = "6.3.4"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kcmutils-devel",
    "kconfig-devel",
    "kdbusaddons-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "ksvg-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "layer-shell-qt-devel",
    "libkscreen-devel",
    "libplasma-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtsensors-devel",
    "xcb-util-devel",
]
depends = ["kdeclarative"]
pkgdesc = "KDE screen management"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/kscreen"
source = f"$(KDE_SITE)/plasma/{pkgver}/kscreen-{pkgver}.tar.xz"
sha256 = "99af84cb5b8e14a8945dfff20e7acd4245cae9f1c7cd311f3eee8dd22c100b25"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
