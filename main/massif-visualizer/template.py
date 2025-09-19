pkgname = "massif-visualizer"
pkgver = "25.08.1"
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
sha256 = "a9e8fd6ae941bc5f2f55cab64d58e2229dddff1ce4129acabc382f175f557d90"
