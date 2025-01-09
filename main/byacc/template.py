pkgname = "byacc"
pkgver = "20241231"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--program-transform=s,^,b,"]
configure_gen = []
pkgdesc = "Berkeley yacc, a LALR(1) parser generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:byacc"
url = "http://invisible-island.net/byacc"
source = f"https://invisible-island.net/archives/byacc/byacc-{pkgver}.tgz"
sha256 = "192c2fae048d4e7f514ba451627f9c4e612765099f819c19191f9fde3e609673"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("README")
    self.install_license("LICENSE")
    self.install_link("usr/bin/yacc", "byacc")
    self.install_link("usr/share/man/man1/yacc.1", "byacc.1")
