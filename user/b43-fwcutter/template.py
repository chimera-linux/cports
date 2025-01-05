pkgname = "b43-fwcutter"
pkgver = "019"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Tool to extract firmware for Broadcom 43xx wireless chips"
maintainer = "breakgimme <adam@plock.com>"
license = "BSD-2-Clause"
url = "https://wireless.docs.kernel.org/en/latest/en/users/drivers/b43.html"
source = f"https://bues.ch/b43/fwcutter/b43-fwcutter-{pkgver}.tar.bz2"
sha256 = "d6ea85310df6ae08e7f7e46d8b975e17fc867145ee249307413cfbe15d7121ce"
# no tests
options = ["!check"]


def install(self):
    self.install_license("COPYING")
    self.install_bin("b43-fwcutter")
    self.install_man("b43-fwcutter.1")
