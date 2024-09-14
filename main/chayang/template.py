pkgname = "chayang"
pkgver = "0.1.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "wayland-devel",
]
makedepends = [
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Gradually dim the screen"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://git.sr.ht/~emersion/chayang"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "61aa0e2955e8b5cf321ef14a5fd72f0e953da51a390d456e929b74fc5efcb74a"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
