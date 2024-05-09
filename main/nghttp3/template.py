pkgname = "nghttp3"
pkgver = "1.3.0"
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
sha256 = "450525981d302f23832b18edd1a62cf58019392ca6402408d0eb1a7f3fd92ecf"


def post_install(self):
    self.install_license("COPYING")


@subpackage("nghttp3-devel")
def _devel(self):
    return self.default_devel()
