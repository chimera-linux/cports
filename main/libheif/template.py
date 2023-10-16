pkgname = "libheif"
pkgver = "1.17.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DWITH_DAV1D=ON",
    "-DWITH_JPEG_DECODER=ON",
    "-DWITH_JPEG_ENCODER=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "dav1d-devel",
    "gdk-pixbuf-devel",
    "libaom-devel",
    "libde265-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "x265-devel",
]
pkgdesc = "HEIF and AVIF file format decoder and encoder"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "http://www.libheif.org"
source = f"https://github.com/strukturag/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "80185d9e7319ab2ae622a131eea11b4d573e2ece38f5a1586cf4d1ffd66bb4d7"
hardening = ["!cfi"]  # TODO
# needs full symbol visibility
options = ["!check"]


@subpackage("libheif-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libheif-progs")
def _progs(self):
    return self.default_progs()
