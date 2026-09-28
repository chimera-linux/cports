pkgname = "sord"
pkgver = "0.16.22"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["serd-devel", "pcre2-devel", "zix-devel"]
pkgdesc = "C library for storing RDF data in memory"
license = "ISC"
url = "https://drobilla.net/software/sord.html"
source = f"https://download.drobilla.net/sord-{pkgver}.tar.xz"
sha256 = "bb23b34b216579136795d518cffa73d91cf205594ce9accebfd408afb839173f"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("sord-devel")
def _(self):
    return self.default_devel()


@subpackage("sord-progs")
def _(self):
    return self.default_progs()
