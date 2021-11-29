pkgname = "wayland-protocols"
pkgver = "1.23"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://github.com/wayland-project/{pkgname}/archive/{pkgver}.tar.gz"
sha256 = "1ffd6f90eb247ff79de50ac10490ed03100572fb571cebef4df9ec74a271b2af"
options = ["lto"]

def post_install(self):
    self.install_license("COPYING")
