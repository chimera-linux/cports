pkgname = "bluez-headers"
pkgver = "5.82"
pkgrel = 0
depends = ["!bluez-devel"]
pkgdesc = "Linux Bluetooth stack"
subdesc = "header files"
license = "LGPL-2.1-or-later"
url = "http://www.bluez.org"
source = f"$(KERNEL_SITE)/bluetooth/bluez-{pkgver}.tar.xz"
sha256 = "0739fa608a837967ee6d5572b43fb89946a938d1c6c26127158aaefd743a790b"


def install(self):
    for f in [
        "bluetooth",
        "bnep",
        "cmtp",
        "hci",
        "hci_lib",
        "hidp",
        "l2cap",
        "rfcomm",
        "sco",
        "sdp",
        "sdp_lib",
    ]:
        self.install_file(f"lib/{f}.h", "usr/include/bluetooth")
