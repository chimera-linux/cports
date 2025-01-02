pkgname = "mythes"
pkgver = "1.2.4"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["hunspell-devel"]
pkgdesc = "Simple thesaurus that uses structured text data"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://sourceforge.net/projects/hunspell/files/MyThes"
source = f"$(SOURCEFORGE_SITE)/hunspell/mythes-{pkgver}.tar.gz"
sha256 = "1e81f395d8c851c3e4e75b568e20fa2fa549354e75ab397f9de4b0e0790a305f"


def post_extract(self):
    # autoreconf needs it
    (self.cwd / "NEWS").touch()


def post_install(self):
    self.install_license("COPYING")


@subpackage("mythes-devel")
def _(self):
    return self.default_devel()
