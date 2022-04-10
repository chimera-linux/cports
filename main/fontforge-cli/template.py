pkgname = "fontforge-cli"
pkgver = "20220308"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_GUI=OFF"]
hostmakedepends = ["cmake", "ninja", "gettext-tiny", "pkgconf"]
makedepends = [
    "python-devel", "libedit-devel", "zlib-devel", "giflib-devel",
    "libpng-devel", "libjpeg-turbo-devel", "libtiff-devel", "libxml2-devel",
    "freetype-devel", "libspiro-devel", "libuninameslist-devel", "woff2-devel",
]
depends = ["!fontforge"] # conflicts with gui version
pkgdesc = "Create and modify PostScript, TrueType and SVG fonts (CLI version)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://fontforge.github.io/en-US"
source = f"https://github.com/fontforge/fontforge/archive/{pkgver}.tar.gz"
sha256 = "58bbc759eb102263be835e6c006b1c16b508ba3d0252acd5389062826764f7a5"

def post_install(self):
    for f in (self.cwd / "contrib/cidmap").glob("Adobe-*.cidmap"):
        self.install_file(f, "usr/share/fontforge")
