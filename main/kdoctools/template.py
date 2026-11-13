pkgname = "kdoctools"
pkgver = "6.32.0"
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
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kdoctools-{pkgver}.tar.xz"
sha256 = "431b6cb8c419576ed86d38a2488db35c26b720abf7b6f9bc2cfd28056229a10d"
hardening = ["vis"]
# the "docs" are really common stylesheets that are needed
# by things using kdoctools so make sure they get installed
options = ["!splitdoc"]


@subpackage("kdoctools-devel")
def _(self):
    return self.default_devel()
