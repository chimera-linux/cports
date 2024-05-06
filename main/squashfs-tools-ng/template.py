pkgname = "squashfs-tools-ng"
pkgver = "1.3.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "bzip2-devel",
    "lz4-devel",
    "lzo-devel",
    "xz-devel",
    "zlib-devel",
    "zstd-devel",
]
pkgdesc = "Set of tools and libraries for working with SquashFS images"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later AND GPL-3.0-or-later"
url = "https://infraroot.at/projects/squashfs-tools-ng/index.html"
source = f"https://infraroot.at/pub/squashfs/{pkgname}-{pkgver}.tar.xz"
sha256 = "0728e825f18ce1af0ec0090ae9892665e61590bb94910f12bf0810b874fdce7f"


@subpackage("libsquashfs")
def _libmagic(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("squashfs-tools-ng-devel")
def _devel(self):
    return self.default_devel()
