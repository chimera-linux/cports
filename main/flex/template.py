pkgname = "flex"
pkgver = "2.6.4"
pkgrel = 2
build_style = "gnu_configure"
configure_args = ["--disable-bootstrap", "--disable-shared"]
configure_gen = []
hostmakedepends = ["byacc"]
makedepends = ["byacc"]
depends = ["byacc", self.with_pkgver("flex-devel-static")]
pkgdesc = "Fast Lexical Analyzer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:flex"
url = "https://github.com/westes/flex"
source = f"{url}/releases/download/v{pkgver}/flex-{pkgver}.tar.gz"
sha256 = "e87aae032bf07c26f85ac0ed3250998c37621d95f8bd748b31f15b33c45ee995"
# Required to enable the definition of reallocarray() in stdlib.h
tool_flags = {
    "CFLAGS": ["-D_GNU_SOURCE"],
}
# dfa.c:epsclosure int overflow for ADD_STATE on snort3 sources
hardening = ["!int"]


def post_patch(self):
    self.ln_s("../lib/malloc.h", "src/rpl_malloc.h")
    self.ln_s("../lib/realloc.h", "src/rpl_realloc.h")


def post_install(self):
    self.install_link("usr/bin/lex", "flex")
    self.install_license("COPYING")


@subpackage("flex-devel-static")
def _(self):
    self.depends = []
    self.install_if = [
        self.parent,
        "base-devel",
        "base-devel-static",
    ]
    # transitional
    self.provides = [self.with_pkgver("libfl-devel-static")]

    return self.default_devel()
