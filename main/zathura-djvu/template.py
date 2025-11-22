pkgname = "zathura-djvu"
pkgver = "0.2.11"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "djvulibre-devel",
    "zathura-devel",
]
depends = ["zathura"]
pkgdesc = "Djvu support for zathura"
license = "Zlib"
url = "https://pwmt.org/projects/zathura-djvu"
source = f"{url}/download/zathura-djvu-{pkgver}.tar.xz"
sha256 = "a854d1d98ec54c2847818270506df3c5f0e134175dd01111af8b3ab3982985c4"


def post_install(self):
    self.install_license("LICENSE")
