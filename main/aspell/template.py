pkgname = "aspell"
pkgver = "0.60.8.3"
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
sha256 = "0534eae11132405120d11e46bf595bd5dd189bc124ba77a5dd6aae861b48a162"


@subpackage("aspell-libs")
def _(self):
    return self.default_libs()


@subpackage("aspell-devel")
def _(self):
    return self.default_devel()
