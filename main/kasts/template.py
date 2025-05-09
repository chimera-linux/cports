pkgname = "kasts"
pkgver = "25.04.1"
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
    "kirigami-devel",
    "kirigami-addons-devel",
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
sha256 = "a390ff4c69ee619deea0088599bf2f1788845868ed3df37da7c7cd556d4ba182"
