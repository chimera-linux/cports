pkgname = "recoll"
pkgver = "1.43.12"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dqtgui=false", # skip GUI
    "-Drecollq=true",
    "-Dpython-aspell=true", # keep CLI + Python support
    "-Dsystemd=false" # disable systemd units
]
hostmakedepends = [
    "gettext",
    "meson",
    "ninja",
    "pkgconf",
    "python",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
makedepends = [
    "aspell-devel",
    "file-devel",
    "hunspell-devel",
    "libjpeg-turbo-devel",
    "libtiff-devel",
    "libxslt-devel",
    "python-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
    "xapian-core-devel",
    "zlib-ng-devel",
]
pkgdesc = "Recoll full-text search tool"
license = "GPL-2.0-or-later"
url = "https://www.recoll.org"
source = f"https://www.lesbonscomptes.com/recoll/recoll-{pkgver}.tar.gz"
sha256 = "3e2a538000bab2013b455303d52fbe604eebcef3bb8f60ff968d2cbc92a853e0"

@subpackage("recoll-devel")
def _(self):
    return self.default_devel()
