pkgname = "libdvdread"
pkgver = "6.1.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-libdvdcss"]
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["libdvdcss-devel"]
pkgdesc = "DVD access library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.videolan.org/developers/libdvdread.html"
source = f"https://download.videolan.org/pub/videolan/{pkgname}/{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "ce35454997a208cbe50e91232f0e73fb1ac3471965813a13b8730a8f18a15369"


@subpackage("libdvdread-devel")
def _devel(self):
    return self.default_devel()
