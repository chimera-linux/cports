pkgname = "freetype"
pkgver = "2.11.0"
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
# higher than freetype-bootstrap, since it's the same version
provider_priority = 10
pkgdesc = "Font rendering engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "FTL OR GPL-2.0-or-later"
url = "https://freetype.org"
source = f"$(NONGNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "8bee39bd3968c4804b70614a0a3ad597299ad0e824bc8aad5ce8aaf48067bde7"
# data files missing
options = ["!check", "lto"]

def post_install(self):
    self.install_license("LICENSE.TXT")
    self.install_license("docs/FTL.TXT")

@subpackage("freetype-static")
def _static(self):
    return self.default_static()

@subpackage("freetype-devel")
def _devel(self):
    return self.default_devel()
