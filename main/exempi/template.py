pkgname = "exempi"
pkgver = "2.6.5"
pkgrel = 4
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "slibtool"]
makedepends = ["boost-devel", "libexpat-devel", "zlib-ng-compat-devel"]
pkgdesc = "Library for easy parsing of XMP metadata"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://libopenraw.freedesktop.org/exempi"
source = f"https://libopenraw.freedesktop.org/download/exempi-{pkgver}.tar.bz2"
sha256 = "e9f9a3d42bff73b5eb0f77ec22cd0163c3e21949cc414ad1f19a0465dde41ffe"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("exempi-devel")
def _(self):
    return self.default_devel()
