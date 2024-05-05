pkgname = "wmenu"
pkgver = "0.1.8"
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
sha256 = "0079d3bbe82e0b02035450b4b31609dd5b822116ea4c14979d2e26d91db3c461"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
