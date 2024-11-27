pkgname = "libscfg"
pkgver = "0.1.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
pkgdesc = "C implementation of the scfg config format"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://git.sr.ht/~emersion/libscfg"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "621a91bf233176e0052e9444f0a42696ad1bfda24b25c027c99cb6e693f273d7"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libscfg-devel")
def _(self):
    return self.default_devel()
