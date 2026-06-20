pkgname = "nghttp2"
pkgver = "1.69.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-http3"]
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = [
    "c-ares-devel",
    "jansson-devel",
    "libev-devel",
    "libevent-devel",
    "libxml2-devel",
    "nghttp3-devel",
    "ngtcp2-devel",
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["cppunit-devel"]
pkgdesc = "HTTP/2 C Library"
license = "MIT"
url = "https://nghttp2.org"
source = f"https://github.com/tatsuhiro-t/nghttp2/releases/download/v{pkgver}/nghttp2-{pkgver}.tar.xz"
sha256 = "1fb324b6ec2c56f6bde0658f4139ffd8209fa9e77ce98fd7a5f63af8d0e508ad"
# CFI; reproduces in e.g. libsoup
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("nghttp2-devel")
def _(self):
    return self.default_devel()


@subpackage("nghttp2-progs")
def _(self):
    return self.default_progs()
