pkgname = "gtk4-layer-shell"
pkgver = "1.0.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
    "wayland-progs",
]
makedepends = ["gtk4-devel", "wayland-protocols"]
pkgdesc = "Library to create panels and other desktop components for Wayland"
maintainer = "Val Packett <val@packett.cool>"
license = "MIT"
url = "https://github.com/wmww/gtk4-layer-shell"
source = f"https://github.com/wmww/gtk4-layer-shell/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7fe327dc3740e4b6f5edfd855e23f84b1ac1ec6854b731047b95df7feb46498b"
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
