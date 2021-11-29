pkgname = "libuninameslist"
pkgver = "20211114"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Library of Unicode names and annotation data"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/fontforge/libuninameslist"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "c089c6164f2cef361c3419a07408be72d6b58d6ef224ec226724a9fa93c0d46e"
options = ["lto"]

def pre_configure(self):
    self.do("autoreconf", "-if")

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libuninameslist-static")
def _static(self):
    return self.default_static()

@subpackage("libuninameslist-devel")
def _devel(self):
    return self.default_devel(man = True)
