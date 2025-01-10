pkgname = "kdoctools"
pkgver = "6.10.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "docbook-xsl",
    "extra-cmake-modules",
    "gettext",
    "libxml2-progs",
    "ninja",
    "perl",
    "perl-uri",
]
makedepends = [
    "karchive-devel",
    "ki18n-devel",
    "libxslt-devel",
    "qt6-qtbase-devel",
]
depends = [
    "docbook-xsl",
    "libxml2-progs",
]
pkgdesc = "KDE Documentation generation from docbook"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kdoctools/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kdoctools-{pkgver}.tar.xz"
sha256 = "03fa98e1213235ee4d4839d16e3edb22ee56849b9ab03d140639cf9facb6b038"
hardening = ["vis"]


@subpackage("kdoctools-devel")
def _(self):
    return self.default_devel()
