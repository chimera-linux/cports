pkgname = "calc"
pkgver = "2.15.1.0"
pkgrel = 0
build_style = "makefile"
make_install_args = ["T=${DESTDIR}"]
make_check_target = "chk"
make_use_env = True
hostmakedepends = ["bash", "mandoc"]
makedepends = ["readline-devel"]
pkgdesc = "C-style arbitrary precision calculator"
maintainer = "peri <peri@periwinkle.sh>"
license = "LGPL-2.1-only"
url = "http://www.isthe.com/chongo/tech/comp/calc"
source = f"https://github.com/lcn2/calc/releases/download/v{pkgver}/calc-{pkgver}.tar.bz2"
sha256 = "633df610a5f5d2f69ad377e320afc85009052b4acc245f0586cbf932a179e2d6"


def init_build(self):
    self.make_build_args += [f"LCC={self.get_tool('CC')}"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("calc-devel")
def _(self):
    return self.default_devel()
