pkgname = "harfbuzz"
pkgver = "11.3.3"
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
url = "https://harfbuzz.github.io"
source = f"https://github.com/harfbuzz/harfbuzz/releases/download/{pkgver}/harfbuzz-{pkgver}.tar.xz"
sha256 = "e1fbca6b32a91ae91ecd9eb2ca8d47a5bfe2b1cb2e54855ab7a0b464919ef358"
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("harfbuzz-devel")
def _(self):
    return self.default_devel()


@subpackage("harfbuzz-progs")
def _(self):
    return self.default_progs()
