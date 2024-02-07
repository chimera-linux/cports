pkgname = "nghttp3"
pkgver = "1.1.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-cunit"]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = ["cunit-devel"]
pkgdesc = "C HTTP/3 library"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://nghttp2.org/nghttp3"
source = f"https://github.com/ngtcp2/nghttp3/releases/download/v{pkgver}/nghttp3-{pkgver}.tar.xz"
sha256 = "f7ffcf21fb889e7d6a8422a3620deb52a8516364805ec3bd7ef296628ca595cb"


def post_install(self):
    self.install_license("COPYING")


@subpackage("nghttp3-devel")
def _devel(self):
    return self.default_devel()
