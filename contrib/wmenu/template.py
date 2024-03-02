pkgname = "wmenu"
pkgver = "0.1.7"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://git.sr.ht/~adnano/wmenu"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "f86c9bfb32a907d467c59d34123c8e7d55cda08524735b7c640b682830f854b9"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
