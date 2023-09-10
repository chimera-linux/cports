pkgname = "gtk-layer-shell"
pkgver = "0.8.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
    "wayland-progs",
]
makedepends = ["gtk+3-devel"]
pkgdesc = "Library to create panels and other desktop components for Wayland"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-3.0-or-later AND MIT"
url = "https://github.com/wmww/gtk-layer-shell"
source = f"https://github.com/wmww/gtk-layer-shell/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c329fac878a1731cb23ad7365f2f2a35e4ab26e72b4e69458e06afd825baad48"
# vis breaks sumbols
hardening = ["!vis"]
# a few tests fail
# gi fail to cross build
options = ["!check", "!cross"]


def post_install(self):
    self.install_license("LICENSE_MIT.txt")


@subpackage("gtk-layer-shell-devel")
def _devel(self):
    return self.default_devel()
