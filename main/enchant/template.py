pkgname = "enchant"
pkgver = "2.5.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-relocatable", "--disable-static"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["glib-devel", "nuspell-devel", "icu-devel", "libltdl-devel"]
checkdepends = ["unittest-cpp"]
pkgdesc = "Generic spell checking library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://abiword.github.io/enchant"
source = f"https://github.com/AbiWord/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "149e224cdd2ca825d874639578b6246e07f37d5b8f3970658a377a1ef46f2e15"
# missing checkdepends
options = ["!check"]


@subpackage("enchant-devel")
def _devel(self):
    return self.default_devel()


@subpackage("enchant-progs")
def _progs(self):
    return self.default_progs()
