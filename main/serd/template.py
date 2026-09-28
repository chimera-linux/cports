pkgname = "serd"
pkgver = "0.32.10"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "C library for RDF syntax"
license = "ISC"
url = "https://drobilla.net/software/serd.html"
source = f"https://download.drobilla.net/serd-{pkgver}.tar.xz"
sha256 = "b0e93b49e52f01a049475b7886ef140407115a32d3b1e5dc5f95141c88275d1c"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("serd-devel")
def _(self):
    return self.default_devel()


@subpackage("serd-progs")
def _(self):
    return self.default_progs()
