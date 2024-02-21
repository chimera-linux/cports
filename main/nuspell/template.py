pkgname = "nuspell"
pkgver = "5.1.4"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["catch2-devel", "icu-devel"]
pkgdesc = "Fast and safe spell checking software"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://nuspell.github.io"
source = f"https://github.com/nuspell/nuspell/archive/v{pkgver}.tar.gz"
sha256 = "bdf344c5adbcc6797940f8f8cb75cb59f5a3794eb21b9547751a11782a792ef7"
hardening = ["!cfi"]  # TODO


@subpackage("nuspell-devel")
def _devel(self):
    return self.default_devel()


@subpackage("nuspell-progs")
def _progs(self):
    return self.default_progs()
