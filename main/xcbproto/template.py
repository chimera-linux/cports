pkgname = "xcbproto"
pkgver = "1.16.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--enable-legacy"]
hostmakedepends = ["pkgconf", "python", "automake"]
depends = ["python"]
pkgdesc = "XML-XCB (X C Bindings) protocol descriptions"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"https://gitlab.freedesktop.org/xorg/proto/xcbproto/-/archive/xcb-proto-{pkgver}/{pkgname}-xcb-proto-{pkgver}.tar.gz"
sha256 = "0e88e4a68e28521cab05660c14c320ae32ea7aa64bc498c25557f726ccfda388"


def post_install(self):
    self.install_license("COPYING")
