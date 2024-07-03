pkgname = "nuspell"
pkgver = "5.1.5"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["catch2-devel", "icu-devel"]
pkgdesc = "Fast and safe spell checking software"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://nuspell.github.io"
source = f"https://github.com/nuspell/nuspell/archive/v{pkgver}.tar.gz"
sha256 = "39fa6d9da6797cd711d7981b1f55359c55dfa4a302560e645cb59af6f764401a"
hardening = ["!cfi"]  # TODO


@subpackage("nuspell-devel")
def _devel(self):
    return self.default_devel()


@subpackage("nuspell-progs")
def _progs(self):
    return self.default_progs()
