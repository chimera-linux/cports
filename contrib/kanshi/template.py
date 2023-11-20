pkgname = "kanshi"
pkgver = "1.4.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "varlink-devel",
    "wayland-devel",
]
pkgdesc = "Dynamic display configuration for wayland"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://sr.ht/~emersion/kanshi"
source = f"https://git.sr.ht/~emersion/kanshi/archive/v{pkgver}.tar.gz"
sha256 = "e9be76a969f526bd51217c0465f4f00bdb8ce176c1e58f08c7b2ed1b341ce653"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
