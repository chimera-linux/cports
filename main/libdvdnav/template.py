pkgname = "libdvdnav"
pkgver = "6.1.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libdvdcss-devel", "libdvdread-devel"]
pkgdesc = "DVD navigation library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.videolan.org/developers/libdvdnav.html"
source = f"https://download.videolan.org/pub/videolan/{pkgname}/{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "c191a7475947d323ff7680cf92c0fb1be8237701885f37656c64d04e98d18d48"


@subpackage("libdvdnav-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
