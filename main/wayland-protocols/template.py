pkgname = "wayland-protocols"
pkgver = "1.27"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://github.com/wayland-project/{pkgname}/archive/{pkgver}.tar.gz"
sha256 = "6dd6ee86478adf4347f3b8b4f3da62dbe9e44912c9cef21cf99abfe692313df4"

def post_install(self):
    self.install_license("COPYING")
