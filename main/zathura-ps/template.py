pkgname = "zathura-ps"
pkgver = "0.2.8"
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
source = f"{url}/download/zathura-ps-{pkgver}.tar.xz"
sha256 = "07ca594f7277f9876d0038048418343ea2964028e93c90f9569eff36a8932e4a"
