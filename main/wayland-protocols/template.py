pkgname = "wayland-protocols"
pkgver = "1.38"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://gitlab.freedesktop.org/wayland/wayland-protocols/-/archive/{pkgver}/wayland-protocols-{pkgver}.tar.gz"
sha256 = "a6069948458a1d86cea2b33a9735e67d7524118c32c388d75efb881a9e9d2cd9"


def post_install(self):
    self.install_license("COPYING")
