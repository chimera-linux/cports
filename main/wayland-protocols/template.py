pkgname = "wayland-protocols"
pkgver = "1.37"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://gitlab.freedesktop.org/wayland/wayland-protocols/-/archive/{pkgver}/wayland-protocols-{pkgver}.tar.gz"
sha256 = "c3b215084eb4cf318415533554c2c2714e58ed75847d7c3a8e50923215ffbbf3"


def post_install(self):
    self.install_license("COPYING")
