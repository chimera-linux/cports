pkgname = "libdvdcss"
pkgver = "1.4.3"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool"]
makedepends = ["linux-headers"]
pkgdesc = "Library for accessing DVDs"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.videolan.org/developers/libdvdcss.html"
source = f"https://download.videolan.org/pub/libdvdcss/{pkgver}/libdvdcss-{pkgver}.tar.bz2"
sha256 = "233cc92f5dc01c5d3a96f5b3582be7d5cee5a35a52d3a08158745d3d86070079"


@subpackage("libdvdcss-devel")
def _(self):
    return self.default_devel()
