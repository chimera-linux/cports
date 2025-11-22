pkgname = "zathura-pdf-poppler"
pkgver = "0.3.4"
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
sha256 = "389fd46e27c7bb0ecb266dbdb0dca4aa9c90a5a0ef5096912f8faebeff939813"


def post_install(self):
    self.install_license("LICENSE")
