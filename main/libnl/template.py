pkgname = "libnl"
pkgver = "3.5.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "flex", "bison"]
makedepends = ["linux-headers"]
pkgdesc = "Netlink Protocol Library Suite"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://github.com/thom311/libnl"
source = f"{url}/releases/download/libnl{pkgver.replace('.', '_')}/libnl-{pkgver}.tar.gz"
sha256 = "352133ec9545da76f77e70ccb48c9d7e5324d67f6474744647a7ed382b5e05fa"

@subpackage("libnl-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libnl-progs")
def _progs(self):
    return self.default_progs(man = "18", extra = [
        "usr/lib/libnl",
    ])
