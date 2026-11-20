pkgname = "libicns"
pkgver = "0.8.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "dos2unix", "libtool", "pkgconf"]
makedepends = ["jasper-devel", "libpng-devel"]
pkgdesc = "Library for the translation of the icns format"
license = "LGPL-2.1-or-later"
url = "https://icns.sourceforge.io"
source = f"https://downloads.sf.net/icns/libicns-{pkgver}.tar.gz"
sha256 = "335f10782fc79855cf02beac4926c4bf9f800a742445afbbf7729dab384555c2"


def post_extract(self):
    self.do("dos2unix", "icnsutils/png2icns.c")


@split("devel")
def _(self):
    return self.default_devel()
