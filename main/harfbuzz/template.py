pkgname = "harfbuzz"
pkgver = "8.3.1"
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
sha256 = "f73e1eacd7e2ffae687bc3f056bb0c705b7a05aee86337686e09da8fc1c2030c"
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("harfbuzz-devel")
def _devel(self):
    return self.default_devel()


@subpackage("harfbuzz-progs")
def _progs(self):
    return self.default_progs()
