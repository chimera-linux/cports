pkgname = "libopusenc"
pkgver = "0.2.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = ["opus-devel"]
pkgdesc = "Library for encoding Opus files"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://opus-codec.org"
source = f"https://downloads.xiph.org/releases/opus/libopusenc-{pkgver}.tar.gz"
sha256 = "8298db61a8d3d63e41c1a80705baa8ce9ff3f50452ea7ec1c19a564fe106cbb9"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libopusenc-devel")
def _(self):
    return self.default_devel()
