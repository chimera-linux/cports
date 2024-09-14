pkgname = "fontforge"
pkgver = "20230101"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_GUI=ON"]
hostmakedepends = ["cmake", "gettext", "ninja", "pkgconf"]
makedepends = [
    "freetype-devel",
    "giflib-devel",
    "gtk+3-devel",
    "libedit-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libspiro-devel",
    "libtiff-devel",
    "libuninameslist-devel",
    "libxml2-devel",
    "python-devel",
    "woff2-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Create and modify PostScript, TrueType and SVG fonts"
subdesc = "GUI version"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://fontforge.github.io/en-US"
source = f"https://github.com/fontforge/fontforge/archive/{pkgver}.tar.gz"
sha256 = "ab0c4be41be15ce46a1be1482430d8e15201846269de89df67db32c7de4343f1"
# FIXME int: fails checks
hardening = ["!int"]


def post_install(self):
    for f in (self.cwd / "contrib/cidmap").glob("Adobe-*.cidmap"):
        self.install_file(f, "usr/share/fontforge")
