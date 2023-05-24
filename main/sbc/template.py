pkgname = "sbc"
pkgver = "2.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-pie"]
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["libsndfile-devel", "linux-headers"]
pkgdesc = "Bluetooth Subband Codec (SBC) library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "http://www.bluez.org"
source = f"$(KERNEL_SITE)/bluetooth/{pkgname}-{pkgver}.tar.xz"
sha256 = "8f12368e1dbbf55e14536520473cfb338c84b392939cc9b64298360fd4a07992"


@subpackage("sbc-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
