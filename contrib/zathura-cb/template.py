pkgname = "zathura-cb"
pkgver = "0.1.10"
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
maintainer = "ttyyls <contact@behri.org>"
license = "Zlib"
url = "https://pwmt.org/projects/zathura-cb"
source = f"{url}/download/{pkgname}-{pkgver}.tar.xz"
sha256 = "89b0ca17a80cba1ea9fd1b3b72f3a7173f0aad3a06a8c364d865c4999c18bbc8"


def post_install(self):
    self.install_license("LICENSE")
