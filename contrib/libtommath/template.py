pkgname = "libtommath"
pkgver = "1.2.1"
pkgrel = 0
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
source = f"https://github.com/libtom/libtommath/releases/download/v{pkgver}/ltm-{pkgver}.tar.xz"
sha256 = "986025d7b374276fee2e30e99f3649e4ac0db8a02257a37ee10eae72abed0d1f"
options = ["!cross"]


def do_check(self):
    self.do("gmake", "test_standalone")
    self.do("./test")


@subpackage("libtommath-devel")
def _devel(self):
    return self.default_devel()
