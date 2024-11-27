pkgname = "otf2bdf"
pkgver = "3.1_p1"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "pkgconf",
]
makedepends = ["freetype-devel"]
pkgdesc = "OpenType to BDF font converter"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
# original site is gone
url = "https://github.com/jirutka/otf2bdf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "deb1590c249edf11dda1c7136759b59207ea0ac1c737e1c2d68dedf87c51716e"
# no separate licence file
# no tests
options = ["!distlicense", "!check"]
