pkgname = "kldap"
pkgver = "25.04.3"
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
sha256 = "f08f4a72efe1bcd197b3e63323aa4fa7a09272d408b8a07db4b61c4792e20b7f"


@subpackage("kldap-devel")
def _(self):
    return self.default_devel()
