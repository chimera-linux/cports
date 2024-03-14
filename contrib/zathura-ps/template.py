pkgname = "zathura-ps"
pkgver = "0.2.7"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "libpoppler-devel",
    "libspectre-devel",
    "zathura-devel",
]
depends = ["zathura"]
pkgdesc = "Postscript support for zathura"
maintainer = "ttyyls <contact@behri.org>"
license = "Zlib"
url = "https://pwmt.org/projects/zathura-ps"
source = f"{url}/download/{pkgname}-{pkgver}.tar.xz"
sha256 = "5897f9204cf5f978b9413be7ce7febde843157af48e351938edf07dbf9308e46"
# no tests defined
options = ["!check"]
