pkgname = "swaykbdd"
pkgver = "1.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["json-c-devel"]
pkgdesc = "Keyboard layout switcher for sway"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/artemsen/swaykbdd"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "63c331213f55db9acad2fb2ef41ae7f9091082fb02153cb19d4abf24609a256e"


def post_install(self):
    self.install_license("LICENSE")
