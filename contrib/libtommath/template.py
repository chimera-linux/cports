pkgname = "libtommath"
pkgver = "1.2.0"
pkgrel = 1
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["-f", "makefile.shared"]
make_install_args = ["-f", "makefile.shared"]
make_use_env = True
hostmakedepends = ["pkgconf", "gmake", "libtool"]
pkgdesc = "Portable number theoretic multiple-precision integer library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://www.libtom.net/LibTomMath"
source = f"https://github.com/libtom/{pkgname}/releases/download/v{pkgver}/ltm-{pkgver}.tar.xz"
sha256 = "b7c75eecf680219484055fcedd686064409254ae44bc31a96c5032843c0e18b1"
options = ["!cross"]


def do_check(self):
    self.do("gmake", "test_standalone")
    self.do("./test")


@subpackage("libtommath-devel")
def _devel(self):
    return self.default_devel()
