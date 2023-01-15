pkgname = "freetype"
pkgver = "2.12.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dbrotli=enabled",
    "-Dharfbuzz=enabled",
    "-Dbzip2=enabled",
    "-Dmmap=enabled",
    "-Dpng=enabled",
    "-Dzlib=enabled",
    "-Dtests=enabled",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "harfbuzz-devel", "zlib-devel", "libpng-devel",
    "libbz2-devel", "brotli-devel"
]
pkgdesc = "Font rendering engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "FTL OR GPL-2.0-or-later"
url = "https://freetype.org"
source = f"$(NONGNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "4766f20157cc4cf0cd292f80bf917f92d1c439b243ac3018debf6b9140c41a7f"
# TODO check
hardening = ["!vis"]
# data files missing
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.TXT")
    self.install_license("docs/FTL.TXT")

@subpackage("freetype-devel")
def _devel(self):
    return self.default_devel()
