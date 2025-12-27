pkgname = "fontforge"
pkgver = "20251009"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_GUI=ON"]
hostmakedepends = ["cmake", "gettext", "ninja", "pkgconf"]
makedepends = [
    "freetype-devel",
    "giflib-devel",
    "gtk+3-devel",
    "gtkmm3.0-devel",
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
license = "GPL-3.0-or-later"
url = "http://fontforge.github.io/en-US"
source = f"https://github.com/fontforge/fontforge/archive/{pkgver}.tar.gz"
sha256 = "613424039e0e1b6bb106f8f0df287e1d249ac285d854f4e1964d68e9b9ad7eb0"
# FIXME int: fails checks
hardening = ["!int"]


def post_install(self):
    for f in (self.cwd / "contrib/cidmap").glob("Adobe-*.cidmap"):
        self.install_file(f, "usr/share/fontforge")
