pkgname = "sbc"
pkgver = "1.5"
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
sha256 = "0cbad69823a99e8421fe0700e8cf9eeb8fa0c1ad28e8dbc2182b3353507931d2"

@subpackage("sbc-static")
def _static(self):
    return self.default_static()

@subpackage("sbc-devel")
def _devel(self):
    return self.default_devel(man = True)
