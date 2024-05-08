pkgname = "zathura-djvu"
pkgver = "0.2.9"
pkgrel = 1
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
maintainer = "ttyyls <contact@behri.org>"
license = "Zlib"
url = "https://pwmt.org/projects/zathura-djvu"
source = f"{url}/download/{pkgname}-{pkgver}.tar.xz"
sha256 = "96e6f8a6ee53231073b2f7003264872f84501e63c3da7bf0598d046286b0c200"


def post_install(self):
    self.install_license("LICENSE")
