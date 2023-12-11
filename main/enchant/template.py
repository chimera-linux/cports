pkgname = "enchant"
pkgver = "2.6.4"
pkgrel = 1
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
source = f"https://github.com/AbiWord/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "833b4d5600dbe9ac867e543aac6a7a40ad145351495ca41223d4499d3ddbbd2c"
# missing checkdepends
options = ["!check"]


@subpackage("enchant-devel")
def _devel(self):
    return self.default_devel()


@subpackage("enchant-progs")
def _progs(self):
    return self.default_progs()
