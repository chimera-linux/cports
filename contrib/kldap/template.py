pkgname = "kldap"
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
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kwidgetsaddons-devel",
    "libsasl-devel",
    # "openldap-devel",  # TODO: needed for actual LDAP support
    "qt6-qtdeclarative-devel",
    "qtkeychain-devel",
]
pkgdesc = "KDE LDAP access API"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kldap/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kldap-{pkgver}.tar.xz"
sha256 = "df5796950e68a06166fbf3001f8f45fcece3a7c7aa3c294d0a151377200a19da"


@subpackage("kldap-devel")
def _devel(self):
    return self.default_devel()
