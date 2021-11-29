pkgname = "libwebp"
pkgver = "1.2.1"
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
sha256 = "808b98d2f5b84e9b27fdef6c5372dac769c3bda4502febbfa5031bd3c4d7d018"
options = ["lto"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libwebp-static")
def _static(self):
    return self.default_static()

@subpackage("libwebp-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()

@subpackage("libwebp-progs")
def _progs(self):
    return self.default_progs(man = True)
