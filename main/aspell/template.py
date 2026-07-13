pkgname = "aspell"
pkgver = "0.60.8.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "libtool",
]
pkgdesc = "Spell checker with good multi-language support"
license = "LGPL-2.1-only"
url = "http://aspell.net"
source = f"https://ftp.gnu.org/gnu/aspell/aspell-{pkgver}.tar.gz"
sha256 = "57fe4863eae6048f72245a8575b44b718fb85ca14b9f8c0afc41b254dfd76919"


@subpackage("aspell-libs")
def _(self):
    return self.default_libs()


@subpackage("aspell-devel")
def _(self):
    return self.default_devel()
