pkgname = "byacc"
pkgver = "20210808"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--program-transform=s,^,b,"]
pkgdesc = "Berkeley yacc, a LALR(1) parser generator"
maintainer = "q66 <q66@chimera-linux.org>"
license="custom:byacc"
url = "http://invisible-island.net/byacc"
source = f"ftp://ftp.invisible-island.net/{pkgname}/{pkgname}-{pkgver}.tgz"
sha256 = "f158529be9d0594263c7f11a87616a49ea23e55ac63691252a2304fbbc7d3a83"
options = ["bootstrap"]

def post_install(self):
    self.install_license("README")
    self.install_license("LICENSE")
    self.install_link("byacc", "usr/bin/yacc")
    self.install_link("byacc.1", "usr/share/man/man1/yacc.1")
