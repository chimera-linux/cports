pkgname = "nuspell"
pkgver = "5.1.0"
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
sha256 = "f7a2c151a625cce621c8e4af7de594dd380d5c99b71d998eb3030fa49917753a"
# missing checkdepends
options = ["!check"]

@subpackage("nuspell-devel")
def _devel(self):
    return self.default_devel()

@subpackage("nuspell-progs")
def _progs(self):
    return self.default_progs()
