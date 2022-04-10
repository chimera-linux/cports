pkgname = "libmtp"
pkgver = "1.1.19"
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
sha256 = "deb4af6f63f5e71215cfa7fb961795262920b4ec6cb4b627f55b30b18aa33228"
options = ["!cross"]

@subpackage("libmtp-devel")
def _devel(self):
    self.depends += ["libgcrypt-devel"]

    return self.default_devel()
