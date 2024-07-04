pkgname = "kontrast"
pkgver = "24.05.2"
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
    "qcoro-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "KDE contrast inspection tool"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/kontrast"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kontrast-{pkgver}.tar.xz"
sha256 = "94b750197f28720afd8d435f47de4b14e4841add3fbc663a1ce734830cb7c766"
