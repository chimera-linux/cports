pkgname = "kontrast"
pkgver = "24.08.3"
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
    "kdoctools-devel",
    "ki18n-devel",
    "kirigami-devel",
    "kirigami-addons-devel",
    "qcoro-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "KDE contrast inspection tool"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/kontrast"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kontrast-{pkgver}.tar.xz"
sha256 = "c33d549576d230f9f4a2128bf8a2567fc0366ea8e04327ba61ba9462c24cf9c1"
