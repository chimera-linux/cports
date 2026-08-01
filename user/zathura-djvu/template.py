pkgname = "zathura-djvu"
pkgver = "2026.07.18"
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
sha256 = "451ac83ff99bbcf1e8231abbace77b65793f4ff2bb06e70df053410d454d36a5"


def post_install(self):
    self.install_license("LICENSE")
