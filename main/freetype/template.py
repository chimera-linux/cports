pkgname = "freetype"
pkgver = "2.14.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dbrotli=enabled",
    "-Dbzip2=enabled",
    "-Dharfbuzz=enabled",
    "-Dmmap=enabled",
    "-Dpng=enabled",
    "-Dtests=enabled",
    "-Dzlib=enabled",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "brotli-devel",
    "bzip2-devel",
    "freetype-bootstrap",
    "harfbuzz-devel",
    "libpng-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Font rendering engine"
license = "FTL OR GPL-2.0-or-later"
url = "https://freetype.org"
source = f"$(SOURCEFORGE_SITE)/freetype/freetype-{pkgver}.tar.xz"
sha256 = "32427e8c471ac095853212a37aef816c60b42052d4d9e48230bab3bdf2936ccc"
hardening = ["!vis", "!cfi"]
# data files missing
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.TXT")
    self.install_license("docs/FTL.TXT")


@subpackage("freetype-devel")
def _(self):
    return self.default_devel()
