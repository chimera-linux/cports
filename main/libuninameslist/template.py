pkgname = "libuninameslist"
pkgver = "20221022"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Library of Unicode names and annotation data"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/fontforge/libuninameslist"
source = f"{url}/releases/download/{pkgver}/{pkgname}-dist-{pkgver}.tar.gz"
sha256 = "92c833936d653b2f205fb5e7ac82818311824dabdc7abdc2e81f07c3a0ea39bb"
hardening = ["vis", "cfi"]

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libuninameslist-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
