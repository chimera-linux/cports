pkgname = "wlr-randr"
pkgver = "0.3.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "wayland-devel",
]
pkgdesc = "Utility to manage outputs of wlroots compositors"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "MIT"
url = "https://sr.ht/~emersion/wlr-randr"
source = f"https://git.sr.ht/~emersion/wlr-randr/refs/download/v{pkgver}/wlr-randr-{pkgver}.tar.gz"
sha256 = "37ef025da9653d327bc7bb46c34294171d64749f5e12a3d08d124a2e81b4a089"


def post_install(self):
    self.install_license("LICENSE")
