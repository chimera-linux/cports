pkgname = "kdoctools"
pkgver = "6.2.0"
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
sha256 = "ecf38556ec5f9d99ee2ceb2c28727f4c80342217cb69b9aa945a6f702dc3ff4f"
hardening = ["vis", "cfi"]


@subpackage("kdoctools-devel")
def _devel(self):
    return self.default_devel()
