pkgname = "wayland-protocols"
pkgver = "1.36"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://gitlab.freedesktop.org/wayland/wayland-protocols/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "c839dd4325565fd59a93d6cde17335357328f66983c2e1fb03c33e92d6918b17"


def post_install(self):
    self.install_license("COPYING")
