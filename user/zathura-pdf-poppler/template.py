pkgname = "zathura-pdf-poppler"
pkgver = "2026.05.10"
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
sha256 = "364c38634273c06252087324bf01dbde2885b932795265aee44006aa2701fe23"


def post_install(self):
    self.install_license("LICENSE")
