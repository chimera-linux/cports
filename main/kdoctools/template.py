pkgname = "kdoctools"
pkgver = "6.14.0"
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
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kdoctools/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kdoctools-{pkgver}.tar.xz"
sha256 = "acb9c761e8e10c30f2c32061f64096965459a0513250edf4432f40831a0f536e"
hardening = ["vis"]


@subpackage("kdoctools-devel")
def _(self):
    return self.default_devel()
