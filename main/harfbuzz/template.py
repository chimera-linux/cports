pkgname = "harfbuzz"
pkgver = "11.0.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Db_ndebug=true",
    "-Dcairo=enabled",
    "-Dcpp_std=c++17",
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
license = "MIT"
url = "http://www.freedesktop.org/wiki/Software/HarfBuzz"
source = f"https://github.com/harfbuzz/harfbuzz/releases/download/{pkgver}/harfbuzz-{pkgver}.tar.xz"
sha256 = "f16351bafe214725fe2c1d5b59f0d93e49905a4b247899fb90d70cff953a2b9b"
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("harfbuzz-devel")
def _(self):
    return self.default_devel()


@subpackage("harfbuzz-progs")
def _(self):
    return self.default_progs()
