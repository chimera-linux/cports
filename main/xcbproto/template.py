pkgname = "xcbproto"
pkgver = "1.17.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-legacy"]
hostmakedepends = ["pkgconf", "python", "automake"]
depends = ["python"]
pkgdesc = "XML-XCB (X C Bindings) protocol descriptions"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"https://gitlab.freedesktop.org/xorg/proto/xcbproto/-/archive/xcb-proto-{pkgver}/{pkgname}-xcb-proto-{pkgver}.tar.gz"
sha256 = "479447448281cfb6585ad780f23bd75311af20daf344fb9209c8a87ea77e296a"


def post_install(self):
    self.install_license("COPYING")
