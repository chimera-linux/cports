pkgname = "harfbuzz"
pkgver = "8.2.1"
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
    "meson",
    "pkgconf",
    "glib-devel",
    "gtk-doc-tools",
    "gobject-introspection",
    # prevent installing self through freetype
    "freetype-bootstrap",
]
makedepends = [
    "freetype-bootstrap",
    "cairo-devel",
    "graphite2-devel",
    "icu-devel",
]
pkgdesc = "Text shaping engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.freedesktop.org/wiki/Software/HarfBuzz"
source = f"https://github.com/{pkgname}/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "0fec78f98c9c8faf228957a201c8846f809452c20f8445eb092a1ba6f22dbea5"
# test failures since icu 71
options = ["!cross", "!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("harfbuzz-devel")
def _devel(self):
    return self.default_devel()


@subpackage("harfbuzz-progs")
def _progs(self):
    return self.default_progs()
