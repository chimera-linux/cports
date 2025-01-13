pkgname = "libmikmod"
pkgver = "3.3.12"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
pkgdesc = "Mikmod module player and library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://mikmod.shlomifish.org"
source = f"$(SOURCEFORGE_SITE)/mikmod/libmikmod-{pkgver}.tar.gz"
sha256 = "adef6214863516a4a5b44ebf2c71ef84ecdfeb3444973dacbac70911c9bc67e9"
# CFI: crashes in sc2 ucm
hardening = ["vis", "!cfi"]


@subpackage("libmikmod-devel")
def _(self):
    return self.default_devel(extra=["usr/share/info"])
