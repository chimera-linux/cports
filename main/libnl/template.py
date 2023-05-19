pkgname = "libnl"
pkgver = "3.7.0"
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
sha256 = "9fe43ccbeeea72c653bdcf8c93332583135cda46a79507bfd0a483bb57f65939"

@subpackage("libnl-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libnl-progs")
def _progs(self):
    return self.default_progs(man = "18", extra = [
        "usr/lib/libnl",
    ])

configure_gen = []
