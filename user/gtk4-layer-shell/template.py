pkgname = "gtk4-layer-shell"
pkgver = "1.3.0"
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
sha256 = "1ebb01ab14e98afd1727f68f64981c37bd23305b1f131f5667c02b94cf593192"
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
