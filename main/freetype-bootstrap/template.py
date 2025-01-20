# this package exists so that we can build harfbuzz (and cairo, which harfbuzz
# needs); after that we can build real freetype with harfbuzz support and get
# better hinting - do not actually use this package in a regular system
pkgname = "freetype-bootstrap"
pkgver = "2.13.3"
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
source = f"$(SOURCEFORGE_SITE)/freetype/freetype-{pkgver}.tar.xz"
sha256 = "0550350666d427c74daeb85d5ac7bb353acba5f76956395995311a9c6f063289"
options = ["!lto", "!scanshlibs", "!scanpkgconf", "!autosplit"]


def post_install(self):
    self.install_license("LICENSE.TXT")
    self.install_license("docs/FTL.TXT")
