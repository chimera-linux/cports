pkgname = "byacc"
pkgver = "20230521"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--program-transform=s,^,b,"]
configure_gen = []
pkgdesc = "Berkeley yacc, a LALR(1) parser generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:byacc"
url = "http://invisible-island.net/byacc"
source = (
    f"https://invisible-island.net/archives/{pkgname}/{pkgname}-{pkgver}.tgz"
)
sha256 = "5ad915a7d5833aa38a5e31bd077505666029c35e365dff8569fe4598eaa9fef2"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("README")
    self.install_license("LICENSE")
    self.install_link("byacc", "usr/bin/yacc")
    self.install_link("byacc.1", "usr/share/man/man1/yacc.1")
