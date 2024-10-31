pkgname = "libnl"
pkgver = "3.11.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = ["automake", "libtool", "pkgconf", "flex", "bison"]
makedepends = ["linux-headers"]
pkgdesc = "Netlink Protocol Library Suite"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://github.com/thom311/libnl"
source = f"{url}/releases/download/libnl{pkgver.replace('.', '_')}/libnl-{pkgver}.tar.gz"
sha256 = "2a56e1edefa3e68a7c00879496736fdbf62fc94ed3232c0baba127ecfa76874d"


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
