pkgname = "isl"
pkgver = "0.26"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["gmp-devel"]
pkgdesc = "Integer Set Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://libisl.sourceforge.io"
source = f"$(SOURCEFORGE_SITE)/libisl/isl-{pkgver}.tar.bz2"
sha256 = "5eac8664e9d67be6bd0bee5085d6840b8baf738c06814df47eaf4166d9776436"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("isl-devel")
def _devel(self):
    return self.default_devel()
