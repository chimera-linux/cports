pkgname = "libtirpc"
pkgver = "1.3.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = [
    "heimdal-devel", "libgssglue-devel", "musl-bsd-headers", "linux-headers"
]
pkgdesc = "Transport Independent RPC library (SunRPC replacement)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://sourceforge.net/projects/libtirpc"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "e24eb88b8ce7db3b7ca6eb80115dd1284abc5ec32a8deccfed2224fc2532b9fd"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libtirpc-static")
def _static(self):
    return self.default_static()

@subpackage("libtirpc-devel")
def _devel(self):
    return self.default_devel(man = True)
