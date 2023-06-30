# this package exists so that we can build harfbuzz (and cairo, which harfbuzz
# needs); after that we can build real freetype with harfbuzz support and get
# better hinting - do not actually use this package in a regular system
pkgname = "freetype-bootstrap"
pkgver = "2.13.1"
pkgrel = 0
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
source = f"$(NONGNU_SITE)/freetype/freetype-{pkgver}.tar.xz"
sha256 = "ea67e3b019b1104d1667aa274f5dc307d8cbd606b399bc32df308a77f1a564bf"
options = ["!lto", "!scanshlibs", "!scanpkgconf"]


def post_install(self):
    self.install_license("LICENSE.TXT")
    self.install_license("docs/FTL.TXT")
