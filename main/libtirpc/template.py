pkgname = "libtirpc"
pkgver = "1.3.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "heimdal-devel",
    "linux-headers",
    "musl-bsd-headers",
]
pkgdesc = "Transport Independent RPC library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://sourceforge.net/projects/libtirpc"
source = f"$(SOURCEFORGE_SITE)/libtirpc/libtirpc-{pkgver}.tar.bz2"
sha256 = "bbd26a8f0df5690a62a47f6aa30f797f3ef8d02560d1bc449a83066b5a1d3508"
options = ["linkundefver"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libtirpc-devel")
def _(self):
    return self.default_devel()
