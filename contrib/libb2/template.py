pkgname = "libb2"
pkgver = "0.98.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "BLAKE2 hash library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "CC0-1.0"
url = "https://www.blake2.net"
source = f"https://github.com/BLAKE2/libb2/archive/v{pkgver}.tar.gz"
sha256 = "10053dbc2fa342516b780a6bbf6e7b2a2360b8d49c5ac426936bf3df82526732"


@subpackage("libb2-devel")
def _devel(self):
    return self.default_devel()
