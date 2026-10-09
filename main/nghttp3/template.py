pkgname = "nghttp3"
pkgver = "1.18.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
pkgdesc = "C HTTP/3 library"
license = "MIT"
url = "https://nghttp2.org/nghttp3"
source = f"https://github.com/ngtcp2/nghttp3/releases/download/v{pkgver}/nghttp3-{pkgver}.tar.xz"
sha256 = "aad782c23d3f01bd4bb52c8bac7a553b631ef8115fd1612703df6183449fef19"


def post_install(self):
    self.install_license("COPYING")


@subpackage("nghttp3-devel")
def _(self):
    return self.default_devel()
