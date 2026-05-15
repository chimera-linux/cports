pkgname = "zathura-pdf-poppler"
pkgver = "2026.02.03"
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
sha256 = "e9c35542d5c8de9c5b3a4b83e7dc86cd82bfac90319f472127bacf6651bce77f"


def post_install(self):
    self.install_license("LICENSE")
