pkgname = "kdoctools"
pkgver = "6.3.0"
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
sha256 = "4b50ed15b9dbd08a5b379bd32ed1b47ee80971abbe0c7a2570b749a665c7854a"
hardening = ["vis", "!cfi"]


@subpackage("kdoctools-devel")
def _devel(self):
    return self.default_devel()
