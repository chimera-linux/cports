pkgname = "kontrast"
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
sha256 = "6376ea91635db8eb24dd23798add25b7e7270f0c664a6f0ff543fe0cbb82431e"
