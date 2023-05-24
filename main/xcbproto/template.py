pkgname = "xcbproto"
pkgver = "1.15.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-legacy"]
hostmakedepends = ["pkgconf", "python", "automake"]
depends = ["python"]
pkgdesc = "XML-XCB (X C Bindings) protocol descriptions"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"https://gitlab.freedesktop.org/xorg/proto/{pkgname}/-/archive/xcb-proto-{pkgver}/{pkgname}-xcb-proto-{pkgver}.tar.gz"
sha256 = "7b9370eb5b7b42f6ff0b80f7b9091fa3efba5ffe42dc4a461383dc562dcfd5a6"


def post_install(self):
    self.install_license("COPYING")
