pkgname = "gtk4-layer-shell"
pkgver = "1.2.0"
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
license = "MIT"
url = "https://github.com/wmww/gtk4-layer-shell"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4e04711fec80afbcd0a1e6e39c07ae263d2c3400181791b7826f3e5317b33567"
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
