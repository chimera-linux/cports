pkgname = "wayland-protocols"
pkgver = "1.26"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://github.com/wayland-project/{pkgname}/archive/{pkgver}.tar.gz"
sha256 = "fe56386f436a84e97c3b6a61b76306f205a64425900f247ad0048174b9c32d4d"

def post_install(self):
    self.install_license("COPYING")
