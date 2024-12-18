pkgname = "kasts"
pkgver = "24.12.0"
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
    "ki18n-devel",
    "kirigami-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
    "qtkeychain-devel",
    "syndication-devel",
    "taglib-devel",
    "threadweaver-devel",
]
pkgdesc = "KDE convergent podcast player"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kasts"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kasts-{pkgver}.tar.xz"
sha256 = "48668ee817c68166795f89ec5d51132ee88aeb3d66da1abba1b56f86ed7511a6"
