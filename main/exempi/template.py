pkgname = "exempi"
pkgver = "2.6.1"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake"]
makedepends = ["boost-devel", "libexpat-devel", "zlib-devel"]
pkgdesc = "Library for easy parsing of XMP metadata"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://libopenraw.freedesktop.org/exempi"
source = f"https://libopenraw.freedesktop.org/download/{pkgname}-{pkgver}.tar.bz2"
sha256 = "072451ac1e0dc97ed69a2e5bfc235fd94fe093d837f65584d0e3581af5db18cd"

def post_install(self):
    self.install_license("COPYING")

@subpackage("exempi-devel")
def _devel(self):
    return self.default_devel()
