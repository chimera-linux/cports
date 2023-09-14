pkgname = "libwebp"
pkgver = "1.3.2"
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
sha256 = "2a499607df669e40258e53d0ade8035ba4ec0175244869d1025d460562aa09b4"
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
