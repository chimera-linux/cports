pkgname = "kdoctools"
pkgver = "6.4.0"
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
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kdoctools-{pkgver}.tar.xz"
sha256 = "63e112f907118cafd4584ce8eb3149d3557a7f9e9a4005d10c40cccf46d24dc2"
hardening = ["vis"]


@subpackage("kdoctools-devel")
def _devel(self):
    return self.default_devel()
