pkgname = "zathura-djvu"
pkgver = "2026.02.03"
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
sha256 = "f52c9dff6b8a2865be3e51aebba9ac50a279e1d721dc860b7f6bdfa1e39c1135"


def post_install(self):
    self.install_license("LICENSE")
