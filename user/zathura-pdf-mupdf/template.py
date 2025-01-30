pkgname = "zathura-pdf-mupdf"
pkgver = "0.4.4"
pkgrel = 1
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "mupdf-devel",
    "zathura-devel",
]
checkdepends = ["check-devel"]
depends = ["zathura"]
install_if = ["zathura-mupdf-default"]
pkgdesc = "PDF support for zathura"
maintainer = "ttyyls <contact@behri.org>"
license = "Zlib"
url = "https://pwmt.org/projects/zathura-pdf-mupdf"
source = f"{url}/download/zathura-pdf-mupdf-{pkgver}.tar.xz"
sha256 = "0125624901cabe3a2fe63315a46e7d966a323c028ff53890dfaf7856adb1f4fc"


def post_install(self):
    self.install_license("LICENSE")
