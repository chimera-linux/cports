pkgname = "wlr-randr"
pkgver = "0.4.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "wayland-devel",
]
pkgdesc = "Utility to manage outputs of wlroots compositors"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "MIT"
url = "https://sr.ht/~emersion/wlr-randr"
source = f"https://git.sr.ht/~emersion/wlr-randr/refs/download/v{pkgver}/wlr-randr-{pkgver}.tar.gz"
sha256 = "fd5783002c13d37267898e571f03b618363d13952a264cf3d61a35383869d631"


def post_install(self):
    self.install_license("LICENSE")
