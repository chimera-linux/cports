pkgname = "zathura-pdf-poppler"
pkgver = "2026.07.18"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "poppler-devel",
    "zathura-devel",
]
checkdepends = ["check-devel"]
depends = ["zathura"]
pkgdesc = "PDF support for zathura"
subdesc = "poppler backend"
license = "Zlib"
url = "https://pwmt.org/projects/zathura-pdf-poppler"
source = f"{url}/download/zathura-pdf-poppler-{pkgver}.tar.xz"
sha256 = "605d3f2c2e90efbc0434bb7206f013dc8ff99d8b679c6b519e13543777635bf1"


def post_install(self):
    self.install_license("LICENSE")
