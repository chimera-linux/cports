pkgname = "zathura-djvu"
pkgver = "2026.05.10"
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
sha256 = "a0815efe0e0f9dd01bda9b1348a0202e38b52284039f9f1b406b604f58bd0947"


def post_install(self):
    self.install_license("LICENSE")
