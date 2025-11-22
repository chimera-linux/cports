pkgname = "zathura-ps"
pkgver = "0.2.9"
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
sha256 = "a95334500848a7a6e8f497232abbc63ba4a628796df73766c3714840083555e8"
