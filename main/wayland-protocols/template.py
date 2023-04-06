pkgname = "wayland-protocols"
pkgver = "1.31"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://gitlab.freedesktop.org/wayland/{pkgname}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "04d3f66eca99d638ec8dbfdfdf79334290e22028f7d0b04c7034d9ef18a3248a"

def post_install(self):
    self.install_license("COPYING")
