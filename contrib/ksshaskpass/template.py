pkgname = "ksshaskpass"
pkgver = "6.1.0"
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
    "kcoreaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kwallet-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE askpass helper"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/ksshaskpass"
source = f"$(KDE_SITE)/plasma/{pkgver}/ksshaskpass-{pkgver}.tar.xz"
sha256 = "0a65aa548dd4ecf498978583835d10371048098a623c74ca950c78fc16ea24a9"
