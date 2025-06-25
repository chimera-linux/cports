pkgname = "nghttp2"
pkgver = "1.66.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = [
    "c-ares-devel",
    "jansson-devel",
    "libev-devel",
    "libevent-devel",
    "libxml2-devel",
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["cppunit-devel"]
pkgdesc = "HTTP/2 C Library"
license = "MIT"
url = "https://nghttp2.org"
source = f"https://github.com/tatsuhiro-t/nghttp2/releases/download/v{pkgver}/nghttp2-{pkgver}.tar.xz"
sha256 = "00ba1bdf0ba2c74b2a4fe6c8b1069dc9d82f82608af24442d430df97c6f9e631"
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
