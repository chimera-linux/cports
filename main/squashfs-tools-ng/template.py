pkgname = "squashfs-tools-ng"
pkgver = "1.1.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = [
    "zlib-devel", "liblz4-devel", "liblzma-devel", "libzstd-devel",
    "lzo-devel", "libbz2-devel",
]
pkgdesc = "Set of tools and libraries for working with SquashFS images"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later AND GPL-3.0-or-later"
url = "https://infraroot.at/projects/squashfs-tools-ng/index.html"
source = f"https://infraroot.at/pub/squashfs/{pkgname}-{pkgver}.tar.xz"
sha256 = "6f3f7864f17b250453df31fe3925ce7d1430cf6b1d514112641d734fe3c8f61a"

@subpackage("libsquashfs")
def _libmagic(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()

@subpackage("squashfs-tools-ng-devel")
def _devel(self):
    return self.default_devel()
