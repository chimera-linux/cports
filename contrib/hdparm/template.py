pkgname = "hdparm"
pkgver = "9.65"
pkgrel = 0
build_style = "makefile"
make_install_args = ["-j1", "binprefix=/usr", "sbindir=/usr/bin"]
makedepends = ["linux-headers"]
pkgdesc = "Command-line interface to hard disk drive parameters"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "BSD-1-Clause AND GPL-2.0-only"
url = "https://sourceforge.net/projects/hdparm"
source = f"$(SOURCEFORGE_SITE)/hdparm/hdparm-{pkgver}.tar.gz"
sha256 = "d14929f910d060932e717e9382425d47c2e7144235a53713d55a94f7de535a4b"
hardening = ["vis", "cfi"]
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.TXT")
