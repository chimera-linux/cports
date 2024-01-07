pkgname = "lame"
pkgver = "3.100"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-nasm", "--enable-shared"]
hostmakedepends = ["nasm"]
makedepends = ["ncurses-devel"]
pkgdesc = "Fast, high quality MP3 encoder"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://lame.sourceforge.io"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "ddfe36cab873794038ae2c1210557ad34857a4b6bdc515785d1da9e175b1da1e"


@subpackage("lame-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
