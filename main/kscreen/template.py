pkgname = "kscreen"
pkgver = "6.2.4"
pkgrel = 1
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/kscreen"
source = f"$(KDE_SITE)/plasma/{pkgver}/kscreen-{pkgver}.tar.xz"
sha256 = "3f660c98e698b53a94eab75f55dd56e2aff2dc7ae34c8be69875466599e7b002"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
