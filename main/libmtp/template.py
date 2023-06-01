pkgname = "libmtp"
pkgver = "1.1.21"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-udev=/usr/lib/udev", "--with-udev-group=plugdev"]
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["libgcrypt-devel", "libusb-devel"]
pkgdesc = "Media Transfer Protocol (MTP) library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://libmtp.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "c4ffa5ab8c8f48c91b0047f2e253c101c418d5696a5ed65c839922a4280872a7"
options = ["!cross"]


@subpackage("libmtp-devel")
def _devel(self):
    self.depends += ["libgcrypt-devel"]

    return self.default_devel()
