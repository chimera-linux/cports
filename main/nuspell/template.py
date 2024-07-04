pkgname = "nuspell"
pkgver = "5.1.6"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    # pandoc...
    "-DBUILD_DOCS=OFF",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["catch2-devel", "icu-devel"]
pkgdesc = "Fast and safe spell checking software"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://nuspell.github.io"
source = f"https://github.com/nuspell/nuspell/archive/v{pkgver}.tar.gz"
sha256 = "5d4baa1daf833a18dc06ae0af0571d9574cc849d47daff6b9ce11dac0a5ded6a"
hardening = ["!cfi"]  # TODO


@subpackage("nuspell-devel")
def _devel(self):
    return self.default_devel()


@subpackage("nuspell-progs")
def _progs(self):
    return self.default_progs()
