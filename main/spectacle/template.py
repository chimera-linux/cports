pkgname = "spectacle"
pkgver = "6.7.91"
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
    "kquickimageeditor-devel",
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
    "tesseract-devel",
    "xcb-util-devel",
    "zxing-cpp-devel",
]
pkgdesc = "KDE Screenshot capture utility"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/spectacle"
source = f"$(KDE_UNSTABLE_SITE)/plasma/{pkgver}/spectacle-{pkgver}.tar.xz"
sha256 = "65152b493319b341703009ba8adca4af9557761f6f200e5be3025738c409af23"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
