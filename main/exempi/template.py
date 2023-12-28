pkgname = "exempi"
pkgver = "2.6.5"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool"]
makedepends = ["boost-devel", "libexpat-devel", "zlib-devel"]
pkgdesc = "Library for easy parsing of XMP metadata"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://libopenraw.freedesktop.org/exempi"
source = (
    f"https://libopenraw.freedesktop.org/download/{pkgname}-{pkgver}.tar.bz2"
)
sha256 = "e9f9a3d42bff73b5eb0f77ec22cd0163c3e21949cc414ad1f19a0465dde41ffe"
# FIXME cfi
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("exempi-devel")
def _devel(self):
    return self.default_devel()
