pkgname = "swappy"
pkgver = "1.5.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["gettext", "meson", "pkgconf", "scdoc"]
makedepends = ["cairo-devel", "gtk+3-devel", "pango-devel"]
depends = ["wl-clipboard", "fonts-font-awesome-otf"]
pkgdesc = "Wayland native snapshot editing tool"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "MIT"
url = "https://github.com/jtheoof/swappy"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "266fac289d4b903d80d44746044bafe8a8b663c6032be696c651ad390bcb1850"


def post_install(self):
    self.install_license("LICENSE")
