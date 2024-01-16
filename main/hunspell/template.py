pkgname = "hunspell"
pkgver = "1.7.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-ui", "--with-readline"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["gettext-devel", "ncurses-devel", "libedit-readline-devel"]
checkdepends = ["bash"]
pkgdesc = "Spell checker and morphological analyzer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1"
url = "https://hunspell.github.io"
source = f"https://github.com/hunspell/hunspell/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "11ddfa39afe28c28539fe65fc4f1592d410c1e9b6dd7d8a91ca25d85e9ec65b8"


@subpackage("hunspell-libs")
def _libs(self):
    return self.default_libs()


@subpackage("hunspell-devel")
def _devel(self):
    return self.default_devel()
