pkgname = "zlib"
pkgver = "1.3.1"
pkgrel = 0
build_style = "configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Compression/decompression Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Zlib"
url = "https://www.zlib.net"
source = f"{url}/fossils/{pkgname}-{pkgver}.tar.gz"
sha256 = "9a93b2b7dfdac77ceba5a558a580e74667dd6fede4585b91eefb60f03b72df23"
tool_flags = {"CFLAGS": ["-fPIC"]}
options = ["bootstrap", "linkundefver"]


def do_configure(self):
    self.do(self.chroot_cwd / "configure", "--prefix=/usr", "--shared")


@subpackage("zlib-devel")
def _devel(self):
    return self.default_devel()
