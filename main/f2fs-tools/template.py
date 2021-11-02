pkgname = "f2fs-tools"
pkgver = "1.14.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = [
    "libuuid-devel", "libblkid-devel", "linux-headers", "musl-bsd-headers"
]
pkgdesc = "F2FS (Flash-Friendly File System) utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://git.kernel.org/cgit/linux/kernel/git/jaegeuk/f2fs-tools.git"
source = f"{url}/snapshot/{pkgname}-{pkgver}.tar.gz"
sha256 = "619263d4e2022152a1472c1d912eaae104f20bd227ce0bb9d41d1d6608094bd1"

def pre_configure(self):
    self.do("autoreconf", ["-if"])

@subpackage("f2fs-tools-devel")
def _devel(self):
    return self.default_devel()

@subpackage("f2fs-tools-libs")
def _devel(self):
    return self.default_libs()
