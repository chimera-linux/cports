pkgname = "f2fs-tools"
pkgver = "1.16.0"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "." # bad build system
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = [
    "libuuid-devel", "libblkid-devel", "linux-headers", "musl-bsd-headers"
]
pkgdesc = "F2FS (Flash-Friendly File System) utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://git.kernel.org/cgit/linux/kernel/git/jaegeuk/f2fs-tools.git"
source = f"{url}/snapshot/{pkgname}-{pkgver}.tar.gz"
sha256 = "208c7a07e95383fbd7b466b5681590789dcb41f41bf197369c41a95383b57c5e"

@subpackage("f2fs-tools-devel")
def _devel(self):
    return self.default_devel()

@subpackage("f2fs-tools-libs")
def _devel(self):
    return self.default_libs()
