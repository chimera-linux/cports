pkgname = "harfbuzz"
pkgver = "8.4.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Db_ndebug=true",
    "-Dcairo=enabled",
    "-Ddocs=enabled",
    "-Dfreetype=enabled",
    "-Dglib=enabled",
    "-Dgraphite2=enabled",
    "-Dicu=enabled",
    "-Dintrospection=enabled",
]
hostmakedepends = [
    "glib-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "meson",
    "pkgconf",
    # prevent installing self through freetype
    "freetype-bootstrap",
]
makedepends = [
    "cairo-devel",
    "freetype-bootstrap",
    "graphite2-devel",
    "icu-devel",
]
pkgdesc = "Text shaping engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.freedesktop.org/wiki/Software/HarfBuzz"
source = f"https://github.com/harfbuzz/harfbuzz/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "af4ea73e25ab748c8c063b78c2f88e48833db9b2ac369e29bd115702e789755e"
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("harfbuzz-devel")
def _devel(self):
    return self.default_devel()


@subpackage("harfbuzz-progs")
def _progs(self):
    return self.default_progs()
