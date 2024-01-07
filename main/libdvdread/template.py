pkgname = "libdvdread"
pkgver = "6.1.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-libdvdcss"]
hostmakedepends = ["pkgconf"]
makedepends = ["libdvdcss-devel"]
pkgdesc = "DVD access library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.videolan.org/developers/libdvdread.html"
source = f"https://download.videolan.org/pub/videolan/{pkgname}/{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "cc190f553758ced7571859e301f802cb4821f164d02bfacfd320c14a4e0da763"


@subpackage("libdvdread-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
