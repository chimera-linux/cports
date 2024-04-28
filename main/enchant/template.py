pkgname = "enchant"
pkgver = "2.7.2"
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
sha256 = "7cc3400a6657974a740b6e3c2568e2935c70e5302f07fadb2095366b75ecad6f"
# missing checkdepends
options = ["!check"]


@subpackage("enchant-devel")
def _devel(self):
    return self.default_devel()


@subpackage("enchant-progs")
def _progs(self):
    return self.default_progs()
