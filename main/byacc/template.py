pkgname = "byacc"
pkgver = "20260126"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--program-transform=s,^,b,"]
configure_gen = []
pkgdesc = "Berkeley yacc, a LALR(1) parser generator"
license = "custom:byacc"
url = "http://invisible-island.net/byacc"
source = f"https://invisible-island.net/archives/byacc/byacc-{pkgver}.tgz"
sha256 = "b618c5fb44c2f5f048843db90f7d1b24f78f47b07913c8c7ba8c942d3eb24b00"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("README")
    self.install_license("LICENSE")
    self.install_link("usr/bin/yacc", "byacc")
    self.install_link("usr/share/man/man1/yacc.1", "byacc.1")
