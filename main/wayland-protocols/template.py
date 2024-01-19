pkgname = "wayland-protocols"
pkgver = "1.33"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://gitlab.freedesktop.org/wayland/wayland-protocols/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "71a7d2f062d463aa839497ddfac97e4bd3f00aa306e014f94529aa3a2be193a8"


def post_install(self):
    self.install_license("COPYING")
