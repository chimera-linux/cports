pkgname = "wayland-protocols"
pkgver = "1.32"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://gitlab.freedesktop.org/wayland/{pkgname}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "444b5d823ad0163dfe505c97ea1a0689ca7e2978a87cf59b03f06573b87db260"


def post_install(self):
    self.install_license("COPYING")
