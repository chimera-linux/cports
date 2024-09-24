pkgname = "gtk4-layer-shell"
pkgver = "1.0.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
    "wayland-progs",
]
makedepends = ["gtk4-devel"]
pkgdesc = "Library to create panels and other desktop components for Wayland"
maintainer = "Val Packett <val@packett.cool>"
license = "MIT"
url = "https://github.com/wmww/gtk4-layer-shell"
source = f"https://github.com/wmww/gtk4-layer-shell/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4d669c30b3dbc68ad69ade9752e6ebbe7be132db21a5a4734d42bc09c5481c34"
# vis breaks symbols
hardening = ["!vis"]
# a few tests fail
# gi fail to cross build
options = ["!check", "!cross"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("gtk4-layer-shell-devel")
def _(self):
    return self.default_devel()
