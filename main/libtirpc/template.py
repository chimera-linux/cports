pkgname = "libtirpc"
pkgver = "1.3.5"
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
sha256 = "9b31370e5a38d3391bf37edfa22498e28fe2142467ae6be7a17c9068ec0bf12f"
options = ["linkundefver"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libtirpc-devel")
def _(self):
    return self.default_devel()
