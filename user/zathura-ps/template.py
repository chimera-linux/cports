pkgname = "zathura-ps"
pkgver = "2026.07.18"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "libspectre-devel",
    "poppler-devel",
    "zathura-devel",
]
depends = ["zathura"]
pkgdesc = "Postscript support for zathura"
license = "Zlib"
url = "https://pwmt.org/projects/zathura-ps"
source = f"{url}/download/zathura-ps-{pkgver}.tar.xz"
sha256 = "35a3cabc1617fa53b0def887d04ceef3c62a8bd15ddf6f011be0fe0e6fc60587"
