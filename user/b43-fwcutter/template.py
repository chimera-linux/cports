pkgname = "b43-fwcutter"
pkgver = "020"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Tool to extract firmware for Broadcom 43xx wireless chips"
license = "BSD-2-Clause"
url = "https://wireless.docs.kernel.org/en/latest/en/users/drivers/b43.html"
source = f"https://bues.ch/b43/fwcutter/b43-fwcutter-{pkgver}.tar.xz"
sha256 = "bae58321c0926827b99afd4fddaebbc934c781d8e010fe62e1ddc4af83046214"
# no tests
options = ["!check"]


def install(self):
    self.install_license("COPYING")
    self.install_bin("b43-fwcutter")
    self.install_man("b43-fwcutter.1")
