pkgname = "gtk-layer-shell"
pkgver = "0.9.1"
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
license = "LGPL-3.0-or-later AND MIT"
url = "https://github.com/wmww/gtk-layer-shell"
source = f"https://github.com/wmww/gtk-layer-shell/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "43e2165cf1a9aa8a317b081c2a583648e02389162f1fbbd33836ba27f9ca19fa"
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
