pkgname = "harfbuzz"
pkgver = "4.2.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dglib=enabled",
    "-Dfreetype=enabled",
    "-Dcairo=enabled",
    "-Dicu=enabled",
    "-Dgraphite2=enabled",
    "-Dintrospection=enabled",
    "-Ddocs=enabled",
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gtk-doc-tools",
    "gobject-introspection"
]
makedepends = [
    "freetype-bootstrap", "cairo-devel", "graphite2-devel", "icu-devel"
]
pkgdesc = "Text shaping engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.freedesktop.org/wiki/Software/HarfBuzz"
source = f"https://github.com/{pkgname}/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "f2200f177768bdc21445aa09703326f3bbe8114ac083d081fe1a79d305c7ae73"
options = ["!cross"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("harfbuzz-devel")
def _devel(self):
    return self.default_devel()

@subpackage("harfbuzz-progs")
def _progs(self):
    return self.default_progs()
