pkgname = "kldap"
pkgver = "25.08.2"
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
sha256 = "92067b9cd063c3fd97f6706178781951b9a62861bf31604afbf3fd04c4b7e549"


@subpackage("kldap-devel")
def _(self):
    return self.default_devel()
