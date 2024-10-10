pkgname = "kasts"
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
    "breeze-icons-devel",
    "kcolorscheme-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
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
sha256 = "5646f3f0891f49847bd437e077fe17e0d99be52ecda9e75fb4bbde08789c74e3"
