pkgname = "spectacle"
pkgver = "24.08.2"
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
sha256 = "3f90f8cfe3359ad94f5bb0025a9251805a092c5892cd2a891965c21a0984cbdf"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
