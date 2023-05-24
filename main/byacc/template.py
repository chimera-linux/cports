pkgname = "byacc"
pkgver = "20230219"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--program-transform=s,^,b,"]
pkgdesc = "Berkeley yacc, a LALR(1) parser generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:byacc"
url = "http://invisible-island.net/byacc"
source = (
    f"https://invisible-island.net/archives/{pkgname}/{pkgname}-{pkgver}.tgz"
)
sha256 = "36b972a6d4ae97584dd186925fbbc397d26cb20632a76c2f52ac7653cd081b58"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("README")
    self.install_license("LICENSE")
    self.install_link("byacc", "usr/bin/yacc")
    self.install_link("byacc.1", "usr/share/man/man1/yacc.1")


configure_gen = []
