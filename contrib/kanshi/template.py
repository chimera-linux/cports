pkgname = "kanshi"
pkgver = "1.5.0"
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
sha256 = "303676479dbd944204632e4baf7c20cf74ab8d9b218d98ffc531650632e8fc56"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
