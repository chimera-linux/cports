pkgname = "doasedit"
pkgver = "1.0.7"
pkgrel = 0
depends = ["opendoas"]
pkgdesc = "Shell script to edit files with doas"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://codeberg.org/TotallyLeGIT/doasedit"
source = f"https://codeberg.org/TotallyLeGIT/doasedit/archive/{pkgver}.tar.gz"
sha256 = "300fafa03099b99597ab99d6d1e0376e817e82f1223e3c04c62d8ad8e26c6744"


def install(self):
    self.install_bin("doasedit")
    self.install_license("LICENSE")
