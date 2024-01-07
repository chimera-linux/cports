pkgname = "libdvdcss"
pkgver = "1.4.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Library for accessing DVDs"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.videolan.org/developers/libdvdcss.html"
source = f"https://download.videolan.org/pub/{pkgname}/{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "233cc92f5dc01c5d3a96f5b3582be7d5cee5a35a52d3a08158745d3d86070079"
hardening = ["vis", "cfi"]


@subpackage("libdvdcss-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
