pkgname = "zix"
pkgver = "0.4.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
pkgdesc = "C library of portability wrappers and data structures"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/category/zix"
source = f"https://download.drobilla.net/zix-{pkgver}.tar.xz"
sha256 = "0c071cc11ab030bdc668bea3b46781b6dafd47ddd03b6d0c2bc1ebe7177e488d"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("zix-devel")
def _(self):
    return self.default_devel()
