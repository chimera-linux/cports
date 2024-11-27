pkgname = "gtk-layer-shell"
pkgver = "0.9.0"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-3.0-or-later AND MIT"
url = "https://github.com/wmww/gtk-layer-shell"
source = f"https://github.com/wmww/gtk-layer-shell/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3809e5565d9ed02e44bb73787ff218523e8760fef65830afe60ea7322e22da1c"
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
