pkgname = "kscreen"
pkgver = "6.1.0"
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
    "qt6-qtsensors-devel",
    "xcb-util-devel",
]
depends = ["kdeclarative"]
pkgdesc = "KDE screen management"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/kscreen"
source = f"$(KDE_SITE)/plasma/{pkgver}/kscreen-{pkgver}.tar.xz"
sha256 = "162bd196778cf776ca6469aad05980731fdd8b82570fc045f89612a97abb4401"
# FIXME: cfi breaks both tests like https://paste.c-net.org/zfdjtfn6ssy6
hardening = ["vis", "!cfi"]


def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd/user", recursive=True)
