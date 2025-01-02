pkgname = "wayland-protocols"
pkgver = "1.39"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://gitlab.freedesktop.org/wayland/wayland-protocols/-/archive/{pkgver}/wayland-protocols-{pkgver}.tar.gz"
sha256 = "42c16435dfc83f320ff727b6d446bb0d4feb361dc11796a2c5d3c0fb6532a517"


def post_install(self):
    self.install_license("COPYING")
