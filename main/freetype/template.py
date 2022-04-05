pkgname = "freetype"
pkgver = "2.12.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dbrotli=disabled",
    "-Dharfbuzz=enabled",
    "-Dbzip2=enabled",
    "-Dmmap=enabled",
    "-Dpng=enabled",
    "-Dzlib=enabled",
    "-Dtests=enabled",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["harfbuzz-devel", "zlib-devel", "libpng-devel", "libbz2-devel"]
pkgdesc = "Font rendering engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "FTL OR GPL-2.0-or-later"
url = "https://freetype.org"
source = f"$(NONGNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "ef5c336aacc1a079ff9262d6308d6c2a066dd4d2a905301c4adda9b354399033"
# data files missing
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.TXT")
    self.install_license("docs/FTL.TXT")

@subpackage("freetype-devel")
def _devel(self):
    return self.default_devel()
