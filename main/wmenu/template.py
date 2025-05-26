pkgname = "wmenu"
pkgver = "0.2.0"
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
license = "MIT"
url = "https://codeberg.org/adnano/wmenu"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "4e6aea3f8975fec720f6eb87aad620d5297a8a5a137615e4cf047e95d2b9d308"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
