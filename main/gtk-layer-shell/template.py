pkgname = "gtk-layer-shell"
pkgver = "0.10.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
    "wayland-progs",
]
makedepends = ["gtk+3-devel", "wayland-protocols"]
pkgdesc = "Library to create panels and other desktop components for Wayland"
license = "LGPL-3.0-or-later AND MIT"
url = "https://github.com/wmww/gtk-layer-shell"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ed9bb801d6d9252defba41104820ace595dac824dc8972a758ee2ad134e10505"
# vis breaks sumbols
hardening = ["!vis"]
# a few tests fail
# gi fail to cross build
options = ["!check", "!cross"]


def post_install(self):
    self.install_license("LICENSE_MIT.txt")


@subpackage("gtk-layer-shell-devel")
def _(self):
    return self.default_devel()
