pkgname = "libmtp"
pkgver = "1.1.22"
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
source = f"$(SOURCEFORGE_SITE)/libmtp/libmtp-{pkgver}.tar.gz"
sha256 = "c3fcf411aea9cb9643590cbc9df99fa5fe30adcac695024442973d76fa5f87bc"
options = ["!cross"]


@subpackage("libmtp-devel")
def _(self):
    self.depends += ["libgcrypt-devel"]

    return self.default_devel()
