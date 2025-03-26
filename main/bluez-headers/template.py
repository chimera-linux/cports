pkgname = "bluez-headers"
pkgver = "5.80"
pkgrel = 0
depends = ["!bluez-devel"]
pkgdesc = "Linux Bluetooth stack"
subdesc = "header files"
license = "LGPL-2.1-or-later"
url = "http://www.bluez.org"
source = f"$(KERNEL_SITE)/bluetooth/bluez-{pkgver}.tar.xz"
sha256 = "a4d0bca3299691f06d5bd9773b854638204a51a5026c42b0ad7f1c6cf16b459a"


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
