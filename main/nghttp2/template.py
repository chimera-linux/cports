pkgname = "nghttp2"
pkgver = "1.51.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-python-bindings"]
hostmakedepends = ["pkgconf"]
makedepends = [
    "zlib-devel", "openssl-devel", "libevent-devel", "libev-devel",
    "c-ares-devel", "jansson-devel", "libxml2-devel",
]
checkdepends = ["cppunit-devel"]
pkgdesc = "HTTP/2 C Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://nghttp2.org"
source = f"https://github.com/tatsuhiro-t/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "66aa76d97c143f42295405a31413e5e7d157968dad9f957bb4b015b598882e6b"
# FIXME cfi; reproduces in e.g. libsoup
hardening = ["!cfi"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("nghttp2-devel")
def _devel(self):
    return self.default_devel()
