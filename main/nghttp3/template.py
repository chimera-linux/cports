pkgname = "nghttp3"
pkgver = "1.8.0"
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
sha256 = "a9dd28970977e6802a3eaf2cfaeae6d0fae60c8d2c0f2c4ce600036a7998ee9a"


def post_install(self):
    self.install_license("COPYING")


@subpackage("nghttp3-devel")
def _(self):
    return self.default_devel()
