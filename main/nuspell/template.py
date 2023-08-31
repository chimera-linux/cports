pkgname = "nuspell"
pkgver = "5.1.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON", "-DBUILD_TESTING=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["icu-devel"]
checkdepends = ["catch2"]
pkgdesc = "Fast and safe spell checking software"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://nuspell.github.io"
source = f"https://github.com/{pkgname}/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "2b1c96bdc5a32a17fc8fc24a0c205fa52b0a2920dd6139b0a7d7744cdef48c22"
hardening = ["!cfi"]  # TODO
# missing checkdepends
options = ["!check"]


@subpackage("nuspell-devel")
def _devel(self):
    return self.default_devel()


@subpackage("nuspell-progs")
def _progs(self):
    return self.default_progs()
