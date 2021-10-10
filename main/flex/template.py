pkgname = "flex"
pkgver = "2.6.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-bootstrap", "--disable-shared"]
hostmakedepends = ["byacc", "bsdm4"]
makedepends = ["byacc", "bsdm4"]
depends = ["byacc", f"libfl-devel={pkgver}-r{pkgrel}", "bsdm4"]
pkgdesc = "Fast Lexical Analyzer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:flex"
url = "https://github.com/westes/flex"
source = f"https://github.com/westes/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "e87aae032bf07c26f85ac0ed3250998c37621d95f8bd748b31f15b33c45ee995"

options = ["!check", "!lint"]

# Required to enable the definition of reallocarray() in stdlib.h
tool_flags = {
    "CFLAGS": ["-D_GNU_SOURCE"],
}

def post_install(self):
    self.install_link("flex", "usr/bin/lex")
    self.install_license("COPYING")

@subpackage("libfl-devel")
def _devel(self):
    return self.default_devel()
