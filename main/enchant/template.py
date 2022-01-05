pkgname = "enchant"
pkgver = "2.3.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-relocatable", "--disable-static"]
hostmakedepends = ["pkgconf"]
makedepends = ["libglib-devel", "nuspell-devel", "icu-devel"]
checkdepends = ["unittest-cpp"]
pkgdesc = "Genreic spell checking library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://abiword.github.io/enchant"
source = f"https://github.com/AbiWord/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "ce9ba47fd4d34031bd69445598a698a6611602b2b0e91d705e91a6f5099ead6e"
# missing checkdepends
options = ["!check"]

@subpackage("enchant-devel")
def _devel(self):
    return self.default_devel()

@subpackage("enchant-progs")
def _progs(self):
    return self.default_progs()
