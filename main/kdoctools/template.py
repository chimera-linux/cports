pkgname = "kdoctools"
pkgver = "6.26.0"
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
    "qt6-qttools-devel",
]
depends = ["docbook-xsl", "libxml2-progs"]
provides = [self.with_pkgver("kdoctools-doc")]
pkgdesc = "KDE Documentation generation from docbook"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kdoctools/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kdoctools-{pkgver}.tar.xz"
sha256 = "3fbea5de215076130007f3c18e16b870774ffa4fc85ddace201ac020d0245fb6"
hardening = ["vis"]
# the "docs" are really common stylesheets that are needed
# by things using kdoctools so make sure they get installed
options = ["!splitdoc"]


@subpackage("kdoctools-devel")
def _(self):
    return self.default_devel()
