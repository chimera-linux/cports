pkgname = "byacc"
pkgver = "20240109"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--program-transform=s,^,b,"]
hostmakedepends = ["automake"]
pkgdesc = "Berkeley yacc, a LALR(1) parser generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:byacc"
url = "http://invisible-island.net/byacc"
source = f"https://invisible-island.net/archives/byacc/byacc-{pkgver}.tgz"
sha256 = "f2897779017189f1a94757705ef6f6e15dc9208ef079eea7f28abec577e08446"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("README")
    self.install_license("LICENSE")
    self.install_link("usr/bin/yacc", "byacc")
    self.install_link("usr/share/man/man1/yacc.1", "byacc.1")
