pkgname = "enchant"
pkgver = "2.8.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-relocatable", "--disable-static"]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "libtool",
    "gmake",
    "pkgconf",
    "vala",
]
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
sha256 = "c57add422237b8a7eed116a9a88d8be4f7b9281778fa36f03e1f2c051ecb0372"
# missing checkdepends
options = ["!check"]


@subpackage("enchant-devel")
def _devel(self):
    return self.default_devel()


@subpackage("enchant-progs")
def _progs(self):
    return self.default_progs()
