pkgname = "nghttp3"
pkgver = "1.5.0"
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
sha256 = "8c00e3910ea2ad1218dafebcf8dd2ffdf030c992d9ceb65834d29e5e5278dd0d"


def post_install(self):
    self.install_license("COPYING")


@subpackage("nghttp3-devel")
def _(self):
    return self.default_devel()
