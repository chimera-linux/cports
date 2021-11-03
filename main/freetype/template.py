pkgname = "freetype"
pkgver = "2.11.0"
pkgrel = 0
build_style = "meson"
# FIXME: enable harfbuzz
configure_args = [
    "-Dbrotli=disabled",
    "-Dharfbuzz=disabled",
    "-Dbzip2=enabled",
    "-Dmmap=enabled",
    "-Dpng=enabled",
    "-Dzlib=enabled",
    "-Dtests=enabled",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["zlib-devel", "libpng-devel", "libbz2-devel"]
pkgdesc = "Font rendering engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "FTL OR GPL-2.0-or-later"
url = "https://freetype.org"
source = f"$(NONGNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "8bee39bd3968c4804b70614a0a3ad597299ad0e824bc8aad5ce8aaf48067bde7"
# data files missing
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.TXT")
    self.install_license("docs/FTL.TXT")

@subpackage("freetype-devel")
def _devel(self):
    return self.default_devel()
