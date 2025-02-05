pkgname = "base-devel"
pkgver = "0.2"
pkgrel = 0
build_style = "meta"
pkgdesc = "Base package for development packages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"
options = ["empty"]


@subpackage("base-devel-static")
def _(self):
    self.pkgdesc = "Base package for static development packages"
    self.depends = []
    self.install_if = []
    self.options = ["empty"]

    return []
