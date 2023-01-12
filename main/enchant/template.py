pkgname = "enchant"
pkgver = "2.3.3"
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
sha256 = "3da12103f11cf49c3cf2fd2ce3017575c5321a489e5b9bfa81dd91ec413f3891"
# glib, unmarked api
hardening = ["!vis"]
# missing checkdepends
options = ["!check"]

@subpackage("enchant-devel")
def _devel(self):
    return self.default_devel()

@subpackage("enchant-progs")
def _progs(self):
    return self.default_progs()
