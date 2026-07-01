pkgname = "mythes"
pkgver = "1.2.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["hunspell-devel"]
pkgdesc = "Simple thesaurus that uses structured text data"
license = "BSD-3-Clause"
url = "https://hunspell.github.io"
source = f"https://github.com/hunspell/mythes/releases/download/v{pkgver}/mythes-{pkgver}.tar.xz"
sha256 = "97bd2ba5738aebdba1bc31f30f1be42f1404386c94105ad5990d839a1311c8a5"


def post_extract(self):
    # autoreconf needs it
    (self.cwd / "NEWS").touch()


def post_install(self):
    self.install_license("COPYING")


@subpackage("mythes-devel")
def _(self):
    return self.default_devel()
