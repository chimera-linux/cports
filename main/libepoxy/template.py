pkgname = "libepoxy"
pkgver = "1.5.9"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "xorg-util-macros"]
makedepends = ["mesa-devel"]
pkgdesc = "Library for handling OpenGL function pointers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/anholt/libepoxy"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "ee8048d20179a2e86156ac842ddb6428732d9cd7a2cfc2eca905165bf24887a2"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libepoxy-devel")
def _devel(self):
    return self.default_devel()
