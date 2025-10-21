pkgname = "spectacle"
pkgver = "6.5.1"
pkgrel = 0
build_style = "cmake"
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
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-devel",
    "knotifications-devel",
    "kpipewire-devel",
    "kstatusnotifieritem-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "layer-shell-qt-devel",
    "opencv-devel",
    "plasma-wayland-protocols",
    "prison-devel",
    "purpose-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtmultimedia-devel",
    "qt6-qtwayland-devel",
    "xcb-util-devel",
    "zxing-cpp-devel",
]
pkgdesc = "KDE Screenshot capture utility"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/spectacle"
source = f"$(KDE_SITE)/plasma/{pkgver}/spectacle-{pkgver}.tar.xz"
sha256 = "a46d2e67fba3b129c251271bc6c2463323801ca5566a3c85455307d1f3fbf0ba"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
