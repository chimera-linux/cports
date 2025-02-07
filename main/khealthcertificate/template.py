pkgname = "khealthcertificate"
pkgver = "24.12.2"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/pim/khealthcertificate"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/khealthcertificate-{pkgver}.tar.xz"
sha256 = "707bc132039a4b0493d688f23541b3f7ecaebe69d621bf424231b0655e7c2dc2"


@subpackage("khealthcertificate-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
