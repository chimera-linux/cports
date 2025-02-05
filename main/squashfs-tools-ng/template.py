pkgname = "squashfs-tools-ng"
pkgver = "1.3.2"
pkgrel = 1
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
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Set of tools and libraries for working with SquashFS images"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later AND GPL-3.0-or-later"
url = "https://infraroot.at/projects/squashfs-tools-ng/index.html"
source = f"https://infraroot.at/pub/squashfs/squashfs-tools-ng-{pkgver}.tar.xz"
sha256 = "0d907ac3e735c351e47c867fb51d94bffa3b05fb95bec01f31e848b7c44215a9"


@subpackage("squashfs-tools-ng-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libsquashfs")]

    return self.default_libs()


@subpackage("squashfs-tools-ng-devel")
def _(self):
    return self.default_devel()
