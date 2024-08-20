pkgname = "libnl"
pkgver = "3.10.0"
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
sha256 = "49b3e2235fdb58f5910bbb3ed0de8143b71ffc220571540502eb6c2471f204f5"


@subpackage("libnl-devel")
def _(self):
    return self.default_devel()


@subpackage("libnl-progs")
def _(self):
    return self.default_progs(
        man="18",
        extra=[
            "usr/lib/libnl",
        ],
    )
