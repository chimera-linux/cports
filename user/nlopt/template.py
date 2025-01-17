pkgname = "nlopt"
pkgver = "2.9.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Library for nonlinear optimization"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://nlopt.readthedocs.io"
source = f"https://github.com/stevengj/nlopt/archive/v{pkgver}.tar.gz"
sha256 = "1e6c33f8cbdc4138d525f3326c231f14ed50d99345561e85285638c49b64ee93"


def post_install(self):
    self.install_license("COPYING")


@subpackage("nlopt-devel")
def _(self):
    return self.default_devel()
