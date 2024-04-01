pkgname = "libtirpc"
pkgver = "1.3.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "heimdal-devel",
    "musl-bsd-headers",
    "linux-headers",
]
pkgdesc = "Transport Independent RPC library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://sourceforge.net/projects/libtirpc"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "1e0b0c7231c5fa122e06c0609a76723664d068b0dba3b8219b63e6340b347860"
options = ["linkundefver"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libtirpc-devel")
def _devel(self):
    return self.default_devel()
