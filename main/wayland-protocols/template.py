pkgname = "wayland-protocols"
pkgver = "1.34"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://gitlab.freedesktop.org/wayland/wayland-protocols/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "cd3cc9dedb838e6fc8f55bbeb688e8569ffac7df53bc59dbfac8acbb39267f05"


def post_install(self):
    self.install_license("COPYING")
