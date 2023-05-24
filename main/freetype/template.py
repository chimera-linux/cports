pkgname = "freetype"
pkgver = "2.13.0"
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
    "harfbuzz-devel",
    "zlib-devel",
    "libpng-devel",
    "libbz2-devel",
    "brotli-devel",
]
pkgdesc = "Font rendering engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "FTL OR GPL-2.0-or-later"
url = "https://freetype.org"
source = f"$(NONGNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "5ee23abd047636c24b2d43c6625dcafc66661d1aca64dec9e0d05df29592624c"
hardening = ["!cfi"]  # TODO
# data files missing
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.TXT")
    self.install_license("docs/FTL.TXT")


@subpackage("freetype-devel")
def _devel(self):
    return self.default_devel()
