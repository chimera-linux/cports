pkgname = "wlr-randr"
pkgver = "0.4.0"
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
sha256 = "da6814105e97843d2aedc6d0639b210a571ae85b36aca69ee1ecf173e9652a7a"


def post_install(self):
    self.install_license("LICENSE")
