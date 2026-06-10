pkgname = "zathura-cb"
pkgver = "2026.05.10"
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
sha256 = "32b2fa420fbb8a55f6baca6501fce2820a2acc900453f9b993a3ef84026ae251"


def post_install(self):
    self.install_license("LICENSE")
