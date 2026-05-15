pkgname = "zathura-ps"
pkgver = "2026.02.03"
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
sha256 = "b3556ff2960b7a5d014e873bd0474c37f3f082e370c6ed8efb9487ba6167eda8"
