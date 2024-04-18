pkgname = "enchant"
pkgver = "2.6.9"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--enable-relocatable", "--disable-static"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = [
    "aspell-devel",
    "glib-devel",
    "hunspell-devel",
    "icu-devel",
    "libltdl-devel",
    "nuspell-devel",
]
checkdepends = ["unittest-cpp"]
pkgdesc = "Generic spell checking library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://abiword.github.io/enchant"
source = f"https://github.com/AbiWord/enchant/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "d9a5a10dc9b38a43b3a0fa22c76ed6ebb7e09eb535aff62954afcdbd40efff6b"
# missing checkdepends
options = ["!check"]


@subpackage("enchant-devel")
def _devel(self):
    return self.default_devel()


@subpackage("enchant-progs")
def _progs(self):
    return self.default_progs()
