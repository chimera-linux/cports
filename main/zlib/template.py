pkgname = "zlib"
pkgver = "1.2.13"
pkgrel = 0
build_style = "configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Compression/decompression Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Zlib"
url = "http://www.zlib.net"
source = f"{url}/{pkgname}-{pkgver}.tar.gz"
sha256 = "b3a24de97a8fdbc835b9833169501030b8977031bcb54b3b3ac13740f846ab30"
tool_flags = {"CFLAGS": ["-fPIC"]}
options = ["bootstrap"]


def do_configure(self):
    self.do(self.chroot_cwd / "configure", "--prefix=/usr", "--shared")


@subpackage("zlib-devel")
def _devel(self):
    return self.default_devel()
