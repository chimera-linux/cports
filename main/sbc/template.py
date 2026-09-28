pkgname = "sbc"
pkgver = "2.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-pie"]
hostmakedepends = ["automake", "pkgconf", "slibtool"]
makedepends = ["libsndfile-devel", "linux-headers"]
pkgdesc = "Bluetooth Subband Codec (SBC) library"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "http://www.bluez.org"
source = f"$(KERNEL_SITE)/bluetooth/sbc-{pkgver}.tar.xz"
sha256 = "a1ada76ef35e5af9c2fbd063754dc9e37a8d989417c6eb1ecebb089b1383ae9e"


@subpackage("sbc-devel")
def _(self):
    return self.default_devel()
