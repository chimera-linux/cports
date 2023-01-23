pkgname = "wayland-protocols"
pkgver = "1.29"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://github.com/wayland-project/{pkgname}/archive/{pkgver}.tar.gz"
sha256 = "4a85786ae69cd6d53bbe9278572f3c3d6ea342875ea444960edb6089237c3a18"

def post_install(self):
    self.install_license("COPYING")
