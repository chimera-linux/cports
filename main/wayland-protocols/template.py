pkgname = "wayland-protocols"
pkgver = "1.40"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://gitlab.freedesktop.org/wayland/wayland-protocols/-/archive/{pkgver}/wayland-protocols-{pkgver}.tar.gz"
sha256 = "0d783e6c1fff096d37c4e0fd1f3f14f63c4fdc5c1cf8ec07db2a349ffd56a1d3"


def post_install(self):
    self.install_license("COPYING")
