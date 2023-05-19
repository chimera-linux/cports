pkgname = "libwebp"
pkgver = "1.3.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = [
    "giflib-devel", "libpng-devel", "libtiff-devel", "freeglut-devel"
]
pkgdesc = "WebP image format library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://www.libpng.org/pub/png/libpng.html"
source = f"http://downloads.webmproject.org/releases/webp/{pkgname}-{pkgver}.tar.gz"
sha256 = "64ac4614db292ae8c5aa26de0295bf1623dbb3985054cb656c55e67431def17c"
hardening = ["vis", "cfi"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libwebp-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()

@subpackage("libwebp-progs")
def _progs(self):
    return self.default_progs()

configure_gen = []
