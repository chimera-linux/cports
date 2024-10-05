pkgname = "nghttp3"
pkgver = "1.6.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
pkgdesc = "C HTTP/3 library"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://nghttp2.org/nghttp3"
source = f"https://github.com/ngtcp2/nghttp3/releases/download/v{pkgver}/nghttp3-{pkgver}.tar.xz"
sha256 = "eaa901954bc494034d3738ef19130de69387d6a3da029044c60d9dae91792a8d"


def post_install(self):
    self.install_license("COPYING")


@subpackage("nghttp3-devel")
def _(self):
    return self.default_devel()
