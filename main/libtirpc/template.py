pkgname = "libtirpc"
pkgver = "1.3.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = [
    "heimdal-devel", "libgssglue-devel", "musl-bsd-headers", "linux-headers"
]
pkgdesc = "Transport Independent RPC library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://sourceforge.net/projects/libtirpc"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "6474e98851d9f6f33871957ddee9714fdcd9d8a5ee9abb5a98d63ea2e60e12f3"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libtirpc-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
