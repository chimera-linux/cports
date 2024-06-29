pkgname = "massif-visualizer"
pkgver = "0.8.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/massif_visualizer"
source = f"$(KDE_SITE)/massif-visualizer/{pkgver}/src/massif-visualizer-{pkgver}.tar.xz"
sha256 = "5fad3f0e0d9fbb6bc8cfb744cb4e2c99f231d57ee0dd66dd594d36c2cc588a80"
