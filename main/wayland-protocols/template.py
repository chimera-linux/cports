pkgname = "wayland-protocols"
pkgver = "1.35"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://gitlab.freedesktop.org/wayland/wayland-protocols/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "6e62dfa92ce82487d107b76064cfe2d7ca107c87c239ea9036a763d79c09105a"


def post_install(self):
    self.install_license("COPYING")
