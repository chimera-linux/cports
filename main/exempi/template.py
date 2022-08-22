pkgname = "exempi"
pkgver = "2.6.2"
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
sha256 = "4d17d4c93df2a95da3e3172c45b7a5bf317dd31dafd1c7a340169728c7089d1d"

def post_install(self):
    self.install_license("COPYING")

@subpackage("exempi-devel")
def _devel(self):
    return self.default_devel()
