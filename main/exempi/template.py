pkgname = "exempi"
pkgver = "2.6.6"
pkgrel = 2
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "slibtool"]
makedepends = ["boost-devel", "libexpat-devel", "zlib-ng-compat-devel"]
pkgdesc = "Library for easy parsing of XMP metadata"
license = "BSD-3-Clause"
url = "https://libopenraw.freedesktop.org/exempi"
source = f"https://libopenraw.freedesktop.org/download/exempi-{pkgver}.tar.bz2"
sha256 = "7513b7e42c3bd90a58d77d938c60d2e87c68f81646e7cb8b12d71fe334391c6f"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("exempi-devel")
def _(self):
    return self.default_devel()
