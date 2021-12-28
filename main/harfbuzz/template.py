pkgname = "harfbuzz"
pkgver = "3.1.1"
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
sha256 = "f3f3247bdeabf36765acc237a5f651e651e4e9706582b9cc2cf6c9b8102dfa93"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libharfbuzz")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs(extra = [
        "usr/lib/girepository-1.0"
    ])

@subpackage("harfbuzz-devel")
def _devel(self):
    return self.default_devel()
