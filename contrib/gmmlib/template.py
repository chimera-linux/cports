pkgname = "gmmlib"
pkgver = "22.3.4"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Intel® Graphics Memory Management Library"
maintainer = "eater <=@eater.me>"
license = "MIT"
url = "https://github.com/intel/gmmlib"
source = f"https://github.com/intel/gmmlib/archive/refs/tags/intel-gmmlib-{pkgver}.tar.gz"
sha256 = "c42b5fa1f5f7c165621099b3787de4c052688cd93c6ef986589ab24fff09b659"
# no tests exist
options = ["!check"]

@subpackage("gmmlib-devel")
def _devel(self):
    return self.default_devel()
