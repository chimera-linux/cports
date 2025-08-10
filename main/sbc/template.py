pkgname = "sbc"
pkgver = "2.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-pie"]
hostmakedepends = ["automake", "pkgconf", "slibtool"]
makedepends = ["libsndfile-devel", "linux-headers"]
pkgdesc = "Bluetooth Subband Codec (SBC) library"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "http://www.bluez.org"
source = f"$(KERNEL_SITE)/bluetooth/sbc-{pkgver}.tar.xz"
sha256 = "426633cabd7c798236443516dfa8335b47e004b0ef37ff107e0c7ead3299fcc2"


@subpackage("sbc-devel")
def _(self):
    return self.default_devel()
