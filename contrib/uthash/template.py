pkgname = "uthash"
pkgver = "2.3.0"
pkgrel = 0
pkgdesc = "Hash table for C structures"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://troydhanson.github.io/uthash"
source = (
    f"https://github.com/troydhanson/uthash/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "e10382ab75518bad8319eb922ad04f907cb20cccb451a3aa980c9d005e661acc"


def install(self):
    self.install_files("src", "usr", name="include")
    self.install_license("LICENSE")
