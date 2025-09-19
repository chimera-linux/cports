pkgname = "khealthcertificate"
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
sha256 = "601cededb514b31190896146fdb51c6ee2abe70c4a98094db83535aa4f617746"


@subpackage("khealthcertificate-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
