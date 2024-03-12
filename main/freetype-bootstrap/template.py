# this package exists so that we can build harfbuzz (and cairo, which harfbuzz
# needs); after that we can build real freetype with harfbuzz support and get
# better hinting - do not actually use this package in a regular system
pkgname = "freetype-bootstrap"
pkgver = "2.13.2"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dbrotli=disabled",
    "-Dharfbuzz=disabled",
    "-Dbzip2=disabled",
    "-Dzlib=disabled",
    "-Dpng=disabled",
    "-Dtests=disabled",
    "-Dmmap=enabled",
    "-Ddefault_library=shared",
]
hostmakedepends = ["meson", "pkgconf"]
# conflict with the real stuff
depends = ["!freetype", "!freetype-devel"]
# provide lowest possible version
provides = ["so:libfreetype.so.6=0", "pc:freetype2=24.3.0"]
pkgdesc = "Font rendering engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "FTL OR GPL-2.0-or-later"
url = "https://freetype.org"
source = f"https://de.freedif.org/savannah/freetype/freetype-{pkgver}.tar.xz"
sha256 = "12991c4e55c506dd7f9b765933e62fd2be2e06d421505d7950a132e4f1bb484d"
options = ["!lto", "!scanshlibs", "!scanpkgconf", "!autosplit"]


def post_install(self):
    self.install_license("LICENSE.TXT")
    self.install_license("docs/FTL.TXT")
