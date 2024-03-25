pkgname = "uthash"
pkgver = "2.3.0"
pkgrel = 0
hostmakedepends = ["gmake", "perl"]
pkgdesc = "C macros for hash tables and more"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-2-Clause"
url = "https://troydhanson.github.io/uthash"
source = (
    f"https://github.com/troydhanson/uthash/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "e10382ab75518bad8319eb922ad04f907cb20cccb451a3aa980c9d005e661acc"
options = ["empty"]


def do_check(self):
    self.do("gmake", "-C", "tests")


def do_install(self):
    self.install_license("LICENSE")
    self.install_dir("usr/include")
    self.install_file("src/*.h", "usr/include", glob=True)


@subpackage("uthash-devel")
def _devel(self):
    return self.default_devel()
