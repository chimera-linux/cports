pkgname = "harfbuzz"
pkgver = "12.3.0"
pkgrel = 1
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
url = "https://harfbuzz.github.io"
source = f"https://github.com/harfbuzz/harfbuzz/releases/download/{pkgver}/harfbuzz-{pkgver}.tar.xz"
sha256 = "8660ebd3c27d9407fc8433b5d172bafba5f0317cb0bb4339f28e5370c93d42b7"
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("harfbuzz-devel")
def _(self):
    return self.default_devel()


@subpackage("harfbuzz-progs")
def _(self):
    return self.default_progs()
