pkgname = "spectacle"
pkgver = "24.05.0"
pkgrel = 3
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
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "layer-shell-qt-devel",
    "opencv-devel",
    "plasma-wayland-protocols",
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
sha256 = "def2851e8db3cc00eab0810d988014b15b8f23b474b932b1cdf3c6144326d5aa"
# FIXME: cfi kills app on launch
hardening = ["vis", "!cfi"]


def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd/user", recursive=True)
