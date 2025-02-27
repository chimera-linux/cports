pkgname = "hyphen"
pkgver = "2.8.8"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."  # fails tests otherwise
hostmakedepends = ["automake", "pkgconf", "perl", "gawk", "libtool"]
checkdepends = ["bash"]
pkgdesc = "Hyphenation library"
license = "GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1"
url = "http://sourceforge.net/projects/hunspell/files/Hyphen"
source = f"$(SOURCEFORGE_SITE)/hunspell/hyphen-{pkgver}.tar.gz"
sha256 = "304636d4eccd81a14b6914d07b84c79ebb815288c76fe027b9ebff6ff24d5705"


def post_install(self):
    self.install_license("COPYING")
    self.install_license("COPYING.MPL")


@subpackage("hyphen-devel")
def _(self):
    return self.default_devel()


@subpackage("hyphen-progs")
def _(self):
    return self.default_progs()
