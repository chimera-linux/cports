pkgname = "zathura-pdf-poppler"
pkgver = "0.3.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "libpoppler-devel",
    "zathura-devel",
]
checkdepends = ["check-devel"]
depends = ["zathura"]
pkgdesc = "PDF support for zathura"
subdesc = "poppler backend"
maintainer = "ttyyls <contact@behri.org>"
license = "Zlib"
url = "https://pwmt.org/projects/zathura-pdf-poppler"
source = f"{url}/download/zathura-pdf-poppler-{pkgver}.tar.xz"
sha256 = "c812f2f4446fd5de16734e13c02ea9aa25ba4e3ba9f72b732c0ff90f9ba34935"


def post_install(self):
    self.install_license("LICENSE")
