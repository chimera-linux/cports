pkgname = "libicns"
pkgver = "0.8.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["autoconf", "automake", "libtool", "pkgconf"]
makedepends = ["jasper-devel", "libpng-devel"]
pkgdesc = "Library for the translation of the icns format"
license = "LGPL-2.1-or-later"
url = "https://icns.sourceforge.io"
source = f"https://downloads.sf.net/icns/libicns-{pkgver}.tar.gz"
sha256 = "335f10782fc79855cf02beac4926c4bf9f800a742445afbbf7729dab384555c2"


@subpackage("libicns-devel")
def _(self):
    return self.default_devel()
