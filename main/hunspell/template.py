pkgname = "hunspell"
pkgver = "1.7.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-ui", "--with-readline"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["gettext-devel", "ncurses-devel", "libedit-readline-devel"]
checkdepends = ["bash"]
pkgdesc = "Spell checker and morphological analyzer"
license = "GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1"
url = "https://hunspell.github.io"
source = f"https://github.com/hunspell/hunspell/releases/download/v{pkgver}/hunspell-{pkgver}.tar.gz"
sha256 = "433274dac0619cb00c2e18b43a3dd3a9d50da5b5613fa9b5c21781e35dd76bc1"


@subpackage("hunspell-libs")
def _(self):
    return self.default_libs()


@subpackage("hunspell-devel")
def _(self):
    return self.default_devel()
