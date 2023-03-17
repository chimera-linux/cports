pkgname = "squashfs-tools-ng"
pkgver = "1.2.0"
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
sha256 = "d736076095d584975640a78cd1554ce15ccbdebdd73d779b7d1ec8004832b7e7"

@subpackage("libsquashfs")
def _libmagic(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()

@subpackage("squashfs-tools-ng-devel")
def _devel(self):
    return self.default_devel()
