pkgname = "massif-visualizer"
pkgver = "26.08.3"
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
    "karchive-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdiagram-devel",
    "kgraphviewer-devel",
    "ki18n-devel",
    "kio-devel",
    "kparts-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "KDE visualizer for valgrind massif profile files"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/massif_visualizer"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/massif-visualizer-{pkgver}.tar.xz"
sha256 = "01ce094d0c8c00147a17f8156db78c0f5c31953b6128d4f14d0d4271d035d9d5"
