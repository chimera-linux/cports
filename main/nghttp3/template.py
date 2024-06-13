pkgname = "nghttp3"
pkgver = "1.4.0"
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
sha256 = "c87b27ef33982a3b831dd349f4a75c55bd4c22a8ec0890095b84b54009df9d6a"


def post_install(self):
    self.install_license("COPYING")


@subpackage("nghttp3-devel")
def _devel(self):
    return self.default_devel()
