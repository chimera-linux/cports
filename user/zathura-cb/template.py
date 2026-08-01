pkgname = "zathura-cb"
pkgver = "2026.07.18"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk4-devel",
    "libarchive-devel",
    "zathura-devel",
]
depends = ["zathura"]
pkgdesc = "Comic book support for zathura"
license = "Zlib"
url = "https://pwmt.org/projects/zathura-cb"
source = f"{url}/download/zathura-cb-{pkgver}.tar.xz"
sha256 = "072660fd32ce56ce512655caf8c190ffbf6c3f36ff09b3f740d65150f99ddc13"


def post_install(self):
    self.install_license("LICENSE")
