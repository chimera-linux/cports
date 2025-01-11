pkgname = "spectacle"
pkgver = "24.12.1"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/spectacle"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/spectacle-{pkgver}.tar.xz"
sha256 = "df710e03ebf15133a9760aa0aa83eb1bd85353f7c4a14a834c5f401b094cb999"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
