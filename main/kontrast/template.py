pkgname = "kontrast"
pkgver = "25.12.0"
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
    "futuresql-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "qcoro-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "KDE contrast inspection tool"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/kontrast"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kontrast-{pkgver}.tar.xz"
sha256 = "b73d0b53b50a8a6602cfa067963d84cbef8367cd00fa5c0447d375ce61fd2358"
