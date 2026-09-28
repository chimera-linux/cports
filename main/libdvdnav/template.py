pkgname = "libdvdnav"
pkgver = "6.1.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool"]
makedepends = ["libdvdcss-devel", "libdvdread-devel"]
pkgdesc = "DVD navigation library"
license = "GPL-2.0-or-later"
url = "https://www.videolan.org/developers/libdvdnav.html"
source = f"https://download.videolan.org/pub/videolan/libdvdnav/{pkgver}/libdvdnav-{pkgver}.tar.bz2"
sha256 = "c191a7475947d323ff7680cf92c0fb1be8237701885f37656c64d04e98d18d48"


@subpackage("libdvdnav-devel")
def _(self):
    return self.default_devel()
