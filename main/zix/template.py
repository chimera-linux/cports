pkgname = "zix"
pkgver = "0.6.2"
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
sha256 = "4bc771abf4fcf399ea969a1da6b375f0117784f8fd0e2db356a859f635f616a7"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("zix-devel")
def _(self):
    return self.default_devel()
