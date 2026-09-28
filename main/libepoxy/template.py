pkgname = "libepoxy"
pkgver = "1.5.10"
pkgrel = 1
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "xorg-util-macros"]
makedepends = ["mesa-devel"]
pkgdesc = "Library for handling OpenGL function pointers"
license = "MIT"
url = "https://github.com/anholt/libepoxy"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "a7ced37f4102b745ac86d6a70a9da399cc139ff168ba6b8002b4d8d43c900c15"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libepoxy-devel")
def _(self):
    return self.default_devel()
