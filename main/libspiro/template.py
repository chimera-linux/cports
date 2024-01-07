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
sha256 = "5984fb5af3e4e1f927f3a74850b705a711fb86284802a5e6170b09786440e8be"


@subpackage("libspiro-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
