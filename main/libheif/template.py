pkgname = "libheif"
pkgver = "1.17.5"
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
sha256 = "2150d6f643e36d0c6dc07c203510815c9660c062868f88d6f14cc6a545d6750e"
hardening = ["!cfi"]  # TODO
# needs full symbol visibility
options = ["!check"]


@subpackage("libheif-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libheif-progs")
def _progs(self):
    return self.default_progs()
