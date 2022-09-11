pkgname = "nuspell"
pkgver = "5.1.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["icu-devel"]
checkdepends = ["catch2"]
pkgdesc = "Fast and safe spell checking software"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://nuspell.github.io"
source = f"https://github.com/{pkgname}/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "a65cc7414f0123630bd13b7739eda51484b29f6402086b2db7e0deb846083bb0"
# missing checkdepends
options = ["!check"]

@subpackage("nuspell-devel")
def _devel(self):
    return self.default_devel()

@subpackage("nuspell-progs")
def _progs(self):
    return self.default_progs()
