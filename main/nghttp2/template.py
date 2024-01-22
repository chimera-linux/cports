pkgname = "nghttp2"
pkgver = "1.59.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = [
    "zlib-devel",
    "openssl-devel",
    "libevent-devel",
    "libev-devel",
    "c-ares-devel",
    "jansson-devel",
    "libxml2-devel",
]
checkdepends = ["cppunit-devel"]
pkgdesc = "HTTP/2 C Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://nghttp2.org"
source = f"https://github.com/tatsuhiro-t/nghttp2/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "fdc9bd71f5cf8d3fdfb63066b89364c10eb2fdeab55f3c6755cd7917b2ec4ffb"
# FIXME cfi; reproduces in e.g. libsoup
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("nghttp2-devel")
def _devel(self):
    return self.default_devel()


@subpackage("nghttp2-progs")
def _progs(self):
    return self.default_progs(extra=["usr/share/nghttp2/fetch-ocsp-response"])
