pkgname = "zlib"
pkgver = "1.2.12"
pkgrel = 0
build_style = "configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Compression/decompression Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Zlib"
url = "http://www.zlib.net"
source = f"{url}/{pkgname}-{pkgver}.tar.gz"
sha256 = "91844808532e5ce316b3c010929493c0244f3d37593afd6de04f71821d5136d9"
tool_flags = {"CFLAGS": ["-fPIC"]}
options = ["bootstrap"]

def do_configure(self):
    self.do(self.chroot_cwd / "configure", "--prefix=/usr", "--shared")

@subpackage("zlib-devel")
def _devel(self):
    return self.default_devel()
