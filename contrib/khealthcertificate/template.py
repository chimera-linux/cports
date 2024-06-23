pkgname = "khealthcertificate"
pkgver = "24.05.1"
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
    "openssl-devel",
    "qt6-qtdeclarative-devel",
    "zlib-devel",
]
pkgdesc = "KDE library for health certificates"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/pim/khealthcertificate"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/khealthcertificate-{pkgver}.tar.xz"
sha256 = "10024475e10cb4ac0d20972abe021803eb88fb697bed285873f5fdf8277eb8ff"


@subpackage("khealthcertificate-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
