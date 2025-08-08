pkgname = "nghttp3"
pkgver = "1.11.0"
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
source = f"{url}/releases/download/v{pkgver}/nghttp3-{pkgver}.tar.xz"
sha256 = "27d084518f06d78279b050cc9cdff2418f80fb753da019427ce853cec920f33f"


def post_install(self):
    self.install_license("COPYING")


@subpackage("nghttp3-devel")
def _(self):
    return self.default_devel()
