pkgname = "byacc"
pkgver = "20220128"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--program-transform=s,^,b,"]
pkgdesc = "Berkeley yacc, a LALR(1) parser generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:byacc"
url = "http://invisible-island.net/byacc"
source = f"https://invisible-island.net/archives/{pkgname}/{pkgname}-{pkgver}.tgz"
sha256 = "42c1805cc529314e6a76326fe1b33e80c70862a44b01474da362e2f7db2d749c"

def post_install(self):
    self.install_license("README")
    self.install_license("LICENSE")
    self.install_link("byacc", "usr/bin/yacc")
    self.install_link("byacc.1", "usr/share/man/man1/yacc.1")
