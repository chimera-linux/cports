pkgname = "serd"
pkgver = "0.32.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "C library for RDF syntax"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/software/serd.html"
source = f"https://download.drobilla.net/serd-{pkgver}.tar.xz"
sha256 = "cbefb569e8db686be8c69cb3866a9538c7cb055e8f24217dd6a4471effa7d349"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("serd-devel")
def _(self):
    return self.default_devel()


@subpackage("serd-progs")
def _(self):
    return self.default_progs()
