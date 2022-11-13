pkgname = "wayland-protocols"
pkgver = "1.28"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://github.com/wayland-project/{pkgname}/archive/{pkgver}.tar.gz"
sha256 = "914dfa09e7e866e913b27d2d9bda0e20e728c7b1c831fd3db71538d9f99a4869"

def post_install(self):
    self.install_license("COPYING")
