pkgname = "zathura-cb"
pkgver = "0.1.12"
pkgrel = 1
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
sha256 = "bc62dec4d04d51419192d370ecdf2afa66ba10554c2518abecee0dfce2aac96e"


def post_install(self):
    self.install_license("LICENSE")
