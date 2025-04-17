pkgname = "khealthcertificate"
pkgver = "25.04.0"
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
    "karchive-devel",
    "kcodecs-devel",
    "ki18n-devel",
    "openssl3-devel",
    "qt6-qtdeclarative-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "KDE library for health certificates"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/pim/khealthcertificate"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/khealthcertificate-{pkgver}.tar.xz"
sha256 = "00d589d66ee66c36765fc36c37e0b2c5119836097da61221c859bfdb48fe0f75"


@subpackage("khealthcertificate-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
