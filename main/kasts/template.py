pkgname = "kasts"
pkgver = "26.08.2"
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
    "breeze-icons-devel",
    "kcolorscheme-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "kwindowsystem-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
    "qtkeychain-devel",
    "syndication-devel",
    "taglib-devel",
    "threadweaver-devel",
]
pkgdesc = "KDE convergent podcast player"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kasts"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kasts-{pkgver}.tar.xz"
sha256 = "667c3bfbccfa62a6ac761ae17f0ee617f0f8e74803e134931067940d1a278da1"
