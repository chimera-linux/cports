pkgname = "libwebp"
pkgver = "1.4.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-libwebpdecoder"]
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = [
    "giflib-devel",
    "libpng-devel",
    "libtiff-devel",
    "freeglut-devel",
]
pkgdesc = "WebP image format library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://www.libpng.org/pub/png/libpng.html"
source = (
    f"http://downloads.webmproject.org/releases/webp/{pkgname}-{pkgver}.tar.gz"
)
sha256 = "61f873ec69e3be1b99535634340d5bde750b2e4447caa1db9f61be3fd49ab1e5"
hardening = ["vis"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libwebp-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()


@subpackage("libwebp-progs")
def _progs(self):
    return self.default_progs()
