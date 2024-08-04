pkgname = "zathura-cb"
pkgver = "0.1.11"
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
maintainer = "ttyyls <contact@behri.org>"
license = "Zlib"
url = "https://pwmt.org/projects/zathura-cb"
source = f"{url}/download/zathura-cb-{pkgver}.tar.xz"
sha256 = "4e201ea54cdc20a93258c43556f6389441af99740de7dca6ca1ff524172fbd47"


def post_install(self):
    self.install_license("LICENSE")
