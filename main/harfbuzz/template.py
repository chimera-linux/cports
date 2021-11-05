pkgname = "harfbuzz"
pkgver = "3.1.0"
pkgrel = 0
build_style = "meson"
# FIXME: introspection, docs
configure_args = [
    "-Dglib=enabled",
    "-Dfreetype=enabled",
    "-Dcairo=enabled",
    "-Dicu=enabled",
    "-Dgraphite2=enabled",
    "-Dintrospection=disabled",
    "-Ddocs=disabled",
]
hostmakedepends = ["meson", "pkgconf", "glib-devel"]
makedepends = [
    "freetype-bootstrap", "cairo-devel", "graphite2-devel", "icu-devel"
]
pkgdesc = "Text shaping engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.freedesktop.org/wiki/Software/HarfBuzz"
source = f"https://github.com/{pkgname}/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "2359390944a74a933d2b1bd214754a5b3f817916a09c6d4ca3d263473cf19b8e"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libharfbuzz")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()

@subpackage("harfbuzz-devel")
def _devel(self):
    return self.default_devel()
