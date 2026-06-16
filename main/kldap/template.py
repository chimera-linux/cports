pkgname = "kldap"
pkgver = "26.04.2"
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
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kwidgetsaddons-devel",
    "libsasl-devel",
    "openldap-devel",
    "qt6-qtdeclarative-devel",
    "qtkeychain-devel",
]
pkgdesc = "KDE LDAP access API"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kldap/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kldap-{pkgver}.tar.xz"
sha256 = "5988a3e160ee7c5e4edffd442225a4685a55bbe8d81a7b12c290fb980899120f"


@subpackage("kldap-devel")
def _(self):
    return self.default_devel()
