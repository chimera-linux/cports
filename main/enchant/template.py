pkgname = "enchant"
pkgver = "2.6.7"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-relocatable", "--disable-static"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = [
    "glib-devel",
    "nuspell-devel",
    "hunspell-devel",
    "icu-devel",
    "libltdl-devel",
]
checkdepends = ["unittest-cpp"]
pkgdesc = "Generic spell checking library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://abiword.github.io/enchant"
source = f"https://github.com/AbiWord/enchant/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "a1c2e5b59acca000bbfb24810af4a1165733d407f2154786588e076c8cd57bfc"
# missing checkdepends
options = ["!check"]


@subpackage("enchant-devel")
def _devel(self):
    return self.default_devel()


@subpackage("enchant-progs")
def _progs(self):
    return self.default_progs()
