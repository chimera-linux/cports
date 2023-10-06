pkgname = "libheif"
pkgver = "1.16.2"
pkgrel = 1
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "libde265-devel",
    "x265-devel",
    "libaom-devel",
    "dav1d-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
]
pkgdesc = "HEIF and AVIF file format decoder and encoder"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "http://www.libheif.org"
source = f"https://github.com/strukturag/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "d207f2ff5c86e6af3621c237f186130b985b7a9ff657875944b58ac5d27ba71c"
hardening = ["!cfi"]  # TODO
# needs full symbol visibility
options = ["!check"]


@subpackage("libheif-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libheif-progs")
def _progs(self):
    return self.default_progs()
