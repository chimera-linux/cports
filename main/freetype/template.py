pkgname = "freetype"
pkgver = "2.13.3"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "FTL OR GPL-2.0-or-later"
url = "https://freetype.org"
source = f"$(SOURCEFORGE_SITE)/freetype/freetype-{pkgver}.tar.xz"
sha256 = "0550350666d427c74daeb85d5ac7bb353acba5f76956395995311a9c6f063289"
patch_style = "patch"
hardening = ["!vis", "!cfi"]
# data files missing
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.TXT")
    self.install_license("docs/FTL.TXT")


@subpackage("freetype-devel")
def _(self):
    return self.default_devel()
