pkgname = "byacc"
pkgver = "20210520"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--program-transform=s,^,b,"]
pkgdesc = "Berkeley yacc, a LALR(1) parser generator"
maintainer = "q66 <q66@chimera-linux.org>"
license="custom:byacc"
url = "http://invisible-island.net/byacc"
source = f"ftp://ftp.invisible-island.net/{pkgname}/{pkgname}-{pkgver}.tgz"
sha256 = "d7d31dae72cb973482ef7f975609ae401ccc12ee3fb168b67a69526c60afe43e"
options = ["bootstrap"]

def post_install(self):
    self.install_license("README", "LICENSE")
    self.install_link("byacc", "usr/bin/yacc")
    self.install_link("byacc.1", "usr/share/man/man1/yacc.1")
