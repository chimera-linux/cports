pkgname = "bluez-headers"
pkgver = "5.88"
pkgrel = 0
depends = ["!bluez-devel"]
pkgdesc = "Linux Bluetooth stack"
subdesc = "header files"
license = "LGPL-2.1-or-later"
url = "http://www.bluez.org"
source = f"$(KERNEL_SITE)/bluetooth/bluez-{pkgver}.tar.xz"
sha256 = "6952c39eb5f8b0ee712cc50ab3bcff03be17c410dd97ca640f4849d9a1653ba3"


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
        self.install_file(f"lib/bluetooth/{f}.h", "usr/include/bluetooth")
