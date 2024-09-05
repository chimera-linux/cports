pkgname = "isl"
pkgver = "0.27"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["gmp-devel"]
pkgdesc = "Integer Set Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://libisl.sourceforge.io"
source = f"$(SOURCEFORGE_SITE)/libisl/isl-{pkgver}.tar.bz2"
sha256 = "626335529331f7c89fec493de929e2e92fb3d8cc860fc7af554e0518ee0029ee"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("isl-devel")
def _(self):
    return self.default_devel()
