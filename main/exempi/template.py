pkgname = "exempi"
pkgver = "2.5.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake"]
makedepends = ["boost-devel", "libexpat-devel", "zlib-devel"]
pkgdesc = "Library for easy parsing of XMP metadata"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://libopenraw.freedesktop.org/exempi"
source = f"https://libopenraw.freedesktop.org/download/{pkgname}-{pkgver}.tar.bz2"
sha256 = "52f54314aefd45945d47a6ecf4bd21f362e6467fa5d0538b0d45a06bc6eaaed5"
# FIXME: undefined symbols in test suite?
options = ["!check"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("exempi-devel")
def _devel(self):
    return self.default_devel()
