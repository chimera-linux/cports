pkgname = "cppunit"
pkgver = "1.15.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-werror"]
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
pkgdesc = "C++ unit testing framework"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://cppunit.sourceforge.net"
source = f"https://dev-www.libreoffice.org/src/{pkgname}-{pkgver}.tar.gz"
sha256 = "89c5c6665337f56fd2db36bc3805a5619709d51fb136e51937072f63fcc717a7"

@subpackage("cppunit-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/bin"])

configure_gen = []
