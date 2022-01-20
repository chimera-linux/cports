pkgname = "squashfs-tools-ng"
pkgver = "1.1.3"
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
sha256 = "abce0fcf9a8ae1c3352e4e5e87e1b077f54411da517332ea83b5e7ce948dd70d"

@subpackage("libsquashfs")
def _libmagic(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()

@subpackage("squashfs-tools-ng-devel")
def _devel(self):
    return self.default_devel()
