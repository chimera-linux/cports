pkgname = "zlib"
pkgver = "1.2.11"
pkgrel = 0
build_style = "configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Compression/decompression Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Zlib"
url = "http://www.zlib.net"
source = f"{url}/{pkgname}-{pkgver}.tar.gz"
sha256 = "c3e5e9fdd5004dcb542feda5ee4f0ff0744628baf8ed2dd5d66f8ca1197cb1a1"
tool_flags = {"CFLAGS": ["-fPIC"]}
options = ["bootstrap"]

def do_configure(self):
    self.do(self.chroot_cwd / "configure", [
        "--prefix=/usr", "--shared"
    ])

@subpackage("zlib-devel")
def _devel(self):
    return self.default_devel(man = True)
