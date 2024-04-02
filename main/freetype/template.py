pkgname = "freetype"
pkgver = "2.13.2"
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
    "zlib-devel",
]
pkgdesc = "Font rendering engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "FTL OR GPL-2.0-or-later"
url = "https://freetype.org"
source = f"https://de.freedif.org/savannah/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "12991c4e55c506dd7f9b765933e62fd2be2e06d421505d7950a132e4f1bb484d"
hardening = ["!cfi"]  # TODO
# data files missing
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.TXT")
    self.install_license("docs/FTL.TXT")


@subpackage("freetype-devel")
def _devel(self):
    return self.default_devel()
