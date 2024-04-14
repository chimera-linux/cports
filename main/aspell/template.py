pkgname = "aspell"
pkgver = "0.60.8.1"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "libtool",
]
pkgdesc = "Spell checker with good multi-language support"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "LGPL-2.1-only"
url = "http://aspell.net"
source = f"https://ftp.gnu.org/gnu/aspell/aspell-{pkgver}.tar.gz"
sha256 = "d6da12b34d42d457fa604e435ad484a74b2effcd120ff40acd6bb3fb2887d21b"


@subpackage("aspell-libs")
def _libs(self):
    return self.default_libs()


@subpackage("aspell-devel")
def _devel(self):
    return self.default_devel()
