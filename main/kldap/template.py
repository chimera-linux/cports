pkgname = "kldap"
pkgver = "24.08.2"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kldap/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kldap-{pkgver}.tar.xz"
sha256 = "823a42c7176997d9b8fdbf3140916cf4a8a438de77db68c7ea1031d0cba4feeb"


@subpackage("kldap-devel")
def _(self):
    return self.default_devel()
