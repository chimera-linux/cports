pkgname = "kdoctools"
pkgver = "6.15.0"
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
pkgdesc = "KDE Documentation generation from docbook"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kdoctools/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kdoctools-{pkgver}.tar.xz"
sha256 = "430be5905b0bf6dfb4b7e0e2c0aeb75986eef0a30f13320d9d4cab907fd6bef7"
hardening = ["vis"]


@subpackage("kdoctools-devel")
def _(self):
    return self.default_devel()
