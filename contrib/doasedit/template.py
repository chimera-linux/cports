pkgname = "doasedit"
pkgver = "1.0.6"
pkgrel = 0
depends = ["opendoas"]
pkgdesc = "Shell script to edit files with doas"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://codeberg.org/TotallyLeGIT/doasedit"
source = f"https://codeberg.org/TotallyLeGIT/doasedit/archive/{pkgver}.tar.gz"
sha256 = "bfe0af402b1f2df447a3cecb3027a9176f8de0bbe8f09be9f59a15fcd58e22bf"


def do_install(self):
    self.install_bin("doasedit")
    self.install_license("LICENSE")
