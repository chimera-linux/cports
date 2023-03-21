pkgname = "enchant"
pkgver = "2.3.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-relocatable", "--disable-static"]
hostmakedepends = ["pkgconf"]
makedepends = ["glib-devel", "nuspell-devel", "icu-devel"]
checkdepends = ["unittest-cpp"]
pkgdesc = "Genreic spell checking library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://abiword.github.io/enchant"
source = f"https://github.com/AbiWord/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "1f7e26744db1c9a0fea61d2169f4e5c1ce435cf8c2731c37e3e4054119e994a0"
# missing checkdepends
options = ["!check"]

@subpackage("enchant-devel")
def _devel(self):
    return self.default_devel()

@subpackage("enchant-progs")
def _progs(self):
    return self.default_progs()
