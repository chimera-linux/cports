pkgname = "zathura-cb"
pkgver = "2026.02.03"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "libarchive-devel",
    "zathura-devel",
]
depends = ["zathura"]
pkgdesc = "Comic book support for zathura"
license = "Zlib"
url = "https://pwmt.org/projects/zathura-cb"
source = f"{url}/download/zathura-cb-{pkgver}.tar.xz"
sha256 = "743e37b16b8095c54996afb6a11e4713f0ed3988ed3e1b0bdb8126a2eee83c5c"


def post_install(self):
    self.install_license("LICENSE")
