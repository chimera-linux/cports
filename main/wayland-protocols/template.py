pkgname = "wayland-protocols"
pkgver = "1.25"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://github.com/wayland-project/{pkgname}/archive/{pkgver}.tar.gz"
sha256 = "4326e2b5e04e459ab4522e83e19bff101a3faf9b085bcf46b6cabbd392cc4458"

def post_install(self):
    self.install_license("COPYING")
