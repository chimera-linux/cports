pkgname = "wmenu"
pkgver = "0.1.9"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "cairo-devel",
    "libxkbcommon-devel",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Dynamic menu for wlroots compositors"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://codeberg.org/adnano/wmenu"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "1b457dfdbf8404748a036d8ee4fab1853d5dd28b132531321b7afc78e85bc1cd"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
