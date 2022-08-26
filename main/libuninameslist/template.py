pkgname = "libuninameslist"
pkgver = "20220701"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Library of Unicode names and annotation data"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/fontforge/libuninameslist"
source = f"{url}/releases/download/{pkgver}/{pkgname}-dist-{pkgver}.tar.gz"
sha256 = "3a59cbc626d653e3ab74802da809e56d72cce4017cf5677310c7599eae994cef"

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libuninameslist-devel")
def _devel(self):
    return self.default_devel()
