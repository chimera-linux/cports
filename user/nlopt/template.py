pkgname = "nlopt"
pkgver = "2.7.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Library for nonlinear optimization"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://nlopt.readthedocs.io"
source = f"https://github.com/stevengj/nlopt/archive/v{pkgver}.tar.gz"
sha256 = "db88232fa5cef0ff6e39943fc63ab6074208831dc0031cf1545f6ecd31ae2a1a"


def post_install(self):
    self.install_license("COPYING")


@subpackage("nlopt-devel")
def _(self):
    return self.default_devel()
