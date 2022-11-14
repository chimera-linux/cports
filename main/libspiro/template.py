pkgname = "libspiro"
pkgver = "20221101"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Simplifies the drawing of beautiful curves"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/fontforge/libspiro"
source = f"{url}/releases/download/{pkgver}/{pkgname}-dist-{pkgver}.tar.gz"
sha256 = "3b8e54473f3d4d99c014f2630e62f966f5f4e25c28ca59b63d30bd8e9b7593f5"

@subpackage("libspiro-devel")
def _devel(self):
    return self.default_devel()
