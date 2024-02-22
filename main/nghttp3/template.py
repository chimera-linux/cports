pkgname = "nghttp3"
pkgver = "1.2.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
pkgdesc = "C HTTP/3 library"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://nghttp2.org/nghttp3"
source = f"https://github.com/ngtcp2/nghttp3/releases/download/v{pkgver}/nghttp3-{pkgver}.tar.xz"
sha256 = "d2e216bae7bd7362f850922e4237a5caa204853b3594b22adccab4c1e1c1d1aa"


def post_install(self):
    self.install_license("COPYING")


@subpackage("nghttp3-devel")
def _devel(self):
    return self.default_devel()
