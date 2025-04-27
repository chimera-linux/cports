pkgname = "harfbuzz"
pkgver = "11.1.0"
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
    # prevent installing self through freetype
    "freetype-bootstrap",
    "glib-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "help2man",
    "meson",
    "pkgconf",
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
sha256 = "477f0d48c34dc32093b45304178eb9733361ca1832b5159879c99e6d40227969"
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("harfbuzz-devel")
def _(self):
    return self.default_devel()


@subpackage("harfbuzz-progs")
def _(self):
    return self.default_progs()
