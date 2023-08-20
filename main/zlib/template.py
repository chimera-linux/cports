pkgname = "zlib"
pkgver = "1.3"
pkgrel = 0
build_style = "configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Compression/decompression Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Zlib"
url = "https://www.zlib.net"
source = f"{url}/fossils/{pkgname}-{pkgver}.tar.gz"
sha256 = "ff0ba4c292013dbc27530b3a81e1f9a813cd39de01ca5e0f8bf355702efa593e"
tool_flags = {"CFLAGS": ["-fPIC"]}
options = ["bootstrap"]


def do_configure(self):
    self.do(self.chroot_cwd / "configure", "--prefix=/usr", "--shared")


@subpackage("zlib-devel")
def _devel(self):
    return self.default_devel()
