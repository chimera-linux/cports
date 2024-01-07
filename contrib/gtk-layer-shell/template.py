pkgname = "gtk-layer-shell"
pkgver = "0.8.2"
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
sha256 = "254dd246303127c5d5236ea640f01a82e35d2d652a48d139dd669c832a0f0dce"
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
