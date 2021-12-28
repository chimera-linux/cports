pkgname = "jansson"
pkgver = "2.14"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Library for encoding, decoding and manipulating JSON data"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.digip.org/jansson"
source = f"https://github.com/akheron/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "c739578bf6b764aa0752db9a2fdadcfe921c78f1228c7ec0bb47fa804c55d17b"

def pre_configure(self):
    self.do("autoreconf", "-if")

def post_install(self):
    self.install_license("LICENSE")

@subpackage("jansson-devel")
def _devel(self):
    return self.default_devel()
