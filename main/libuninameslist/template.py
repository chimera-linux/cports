pkgname = "libuninameslist"
pkgver = "20210917"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Library of Unicode names and annotation data"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/fontforge/libuninameslist"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "7d60ea37813590c9d319d53aaac831fedf8067c980167877bc5daa351b378031"

def pre_configure(self):
    self.do("autoreconf", ["-if"])

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libuninameslist-devel")
def _devel(self):
    return self.default_devel(man = True)
