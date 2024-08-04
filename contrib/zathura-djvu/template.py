pkgname = "zathura-djvu"
pkgver = "0.2.10"
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
maintainer = "ttyyls <contact@behri.org>"
license = "Zlib"
url = "https://pwmt.org/projects/zathura-djvu"
source = f"{url}/download/zathura-djvu-{pkgver}.tar.xz"
sha256 = "32e9d89929a76cd7d3fcbaf79f441868bdabedf17317d1d1843faa1f19338d95"


def post_install(self):
    self.install_license("LICENSE")
