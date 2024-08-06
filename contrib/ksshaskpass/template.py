pkgname = "ksshaskpass"
pkgver = "6.1.4"
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
sha256 = "5b72337f939aa81448e892bd3cb62f59bd76d0cd0f9d80700146033fbbd9650c"
