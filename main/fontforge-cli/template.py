pkgname = "fontforge-cli"
pkgver = "20201107"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_GUI=OFF"]
hostmakedepends = ["cmake", "ninja", "gettext-tiny", "pkgconf"]
makedepends = [
    "python-devel", "libedit-devel", "zlib-devel", "giflib-devel",
    "libpng-devel", "libjpeg-turbo-devel", "libtiff-devel", "libxml2-devel",
    "freetype-devel", "libspiro-devel", "libuninameslist-devel",
]
depends = ["!fontforge"] # conflicts with gui version
pkgdesc = "Create and modify PostScript, TrueType and SVG fonts (CLI only)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://fontforge.github.io/en-US"
source = f"https://github.com/fontforge/fontforge/archive/{pkgver}.tar.gz"
sha256 = "274f8c8cbd7b6a1c77d2a1c03d4d6cd3c9319db62be8b8c88fabbf597f7e863c"
options = ["lto"]

def post_install(self):
    for f in (self.cwd / "contrib/cidmap").glob("Adobe-*.cidmap"):
        self.install_file(f, "usr/share/fontforge")
