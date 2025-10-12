pkgname = "kdoctools"
pkgver = "6.19.0"
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
sha256 = "c2048b2979247540f9ba22fd7c6f372ce869699c3a3e81a97af2fa2f733c74bc"
hardening = ["vis"]


@subpackage("kdoctools-devel")
def _(self):
    return self.default_devel()
