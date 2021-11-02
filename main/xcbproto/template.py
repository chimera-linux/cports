pkgname = "xcbproto"
pkgver = "1.14.1"
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
sha256 = "1101be204eecfb6af6b4325c143b3da06a6929753418f161882e86ae1457ca57"

def pre_configure(self):
    self.do("autoreconf", ["-if"])

def post_install(self):
    self.install_license("COPYING")
