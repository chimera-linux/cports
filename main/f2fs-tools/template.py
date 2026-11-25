pkgname = "f2fs-tools"
pkgver = "1.17.0"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."  # bad build system
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = [
    "linux-headers",
    "lz4-devel",
    "lzo-devel",
    "musl-bsd-headers",
    "util-linux-blkid-devel",
    "util-linux-uuid-devel",
]
renames = ["f2fs-tools-libs"]
pkgdesc = "F2FS (Flash-Friendly File System) utilities"
license = "GPL-2.0-only"
url = "https://git.kernel.org/cgit/linux/kernel/git/jaegeuk/f2fs-tools.git"
source = f"{url}/snapshot/f2fs-tools-{pkgver}.tar.gz"
sha256 = "1dbc89ada373b43cc9130b47ad3f575117583ca74715e952046c88a121a2a469"


@subpackage("f2fs-tools-devel")
def _(self):
    return self.default_devel()
