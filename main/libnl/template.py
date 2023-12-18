pkgname = "libnl"
pkgver = "3.9.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
make_cmd = "gmake"
hostmakedepends = ["automake", "gmake", "libtool", "pkgconf", "flex", "bison"]
makedepends = ["linux-headers"]
pkgdesc = "Netlink Protocol Library Suite"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://github.com/thom311/libnl"
source = f"{url}/releases/download/libnl{pkgver.replace('.', '_')}/libnl-{pkgver}.tar.gz"
sha256 = "aed507004d728a5cf11eab48ca4bf9e6e1874444e33939b9d3dfed25018ee9bb"


@subpackage("libnl-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libnl-progs")
def _progs(self):
    return self.default_progs(
        man="18",
        extra=[
            "usr/lib/libnl",
        ],
    )
