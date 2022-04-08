pkgname = "libwebp"
pkgver = "1.2.2"
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
sha256 = "7656532f837af5f4cec3ff6bafe552c044dc39bf453587bd5b77450802f4aee6"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libwebp-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()

@subpackage("libwebp-progs")
def _progs(self):
    return self.default_progs()
