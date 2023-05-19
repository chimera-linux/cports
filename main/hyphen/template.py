pkgname = "hyphen"
pkgver = "2.8.8"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "." # fails tests otherwise
hostmakedepends = ["pkgconf", "perl", "gawk"]
checkdepends = ["bash"]
pkgdesc = "Hyphenation library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1"
url = "http://sourceforge.net/projects/hunspell/files/Hyphen"
source = f"$(SOURCEFORGE_SITE)/hunspell/{pkgname}-{pkgver}.tar.gz"
sha256 = "304636d4eccd81a14b6914d07b84c79ebb815288c76fe027b9ebff6ff24d5705"

def post_install(self):
    self.install_license("COPYING")
    self.install_license("COPYING.MPL")

@subpackage("hyphen-devel")
def _devel(self):
    return self.default_devel()

@subpackage("hyphen-progs")
def _progs(self):
    return self.default_progs()

configure_gen = []
