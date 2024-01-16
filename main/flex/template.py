pkgname = "flex"
pkgver = "2.6.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-bootstrap", "--disable-shared"]
hostmakedepends = ["byacc"]
makedepends = ["byacc"]
depends = ["byacc", f"libfl-devel-static={pkgver}-r{pkgrel}"]
pkgdesc = "Fast Lexical Analyzer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:flex"
url = "https://github.com/westes/flex"
source = f"{url}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "e87aae032bf07c26f85ac0ed3250998c37621d95f8bd748b31f15b33c45ee995"
# Required to enable the definition of reallocarray() in stdlib.h
tool_flags = {
    "CFLAGS": ["-D_GNU_SOURCE"],
}


def post_patch(self):
    self.ln_s("../lib/malloc.h", "src/rpl_malloc.h")
    self.ln_s("../lib/realloc.h", "src/rpl_realloc.h")


def post_install(self):
    self.install_link("flex", "usr/bin/lex")
    self.install_license("COPYING")


@subpackage("libfl-devel-static")
def _static(self):
    self.depends = []
    self.install_if = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "base-devel",
        "base-devel-static",
    ]

    return self.default_devel()


configure_gen = []
