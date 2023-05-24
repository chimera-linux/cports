pkgname = "libmtp"
pkgver = "1.1.20"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-udev=/usr/lib/udev", "--with-udev-group=plugdev"]
hostmakedepends = ["pkgconf"]
makedepends = ["libgcrypt-devel", "libusb-devel"]
pkgdesc = "Media Transfer Protocol (MTP) library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://libmtp.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "c9191dac2f5744cf402e08641610b271f73ac21a3c802734ec2cedb2c6bc56d0"
options = ["!cross"]


@subpackage("libmtp-devel")
def _devel(self):
    self.depends += ["libgcrypt-devel"]

    return self.default_devel()


configure_gen = []
