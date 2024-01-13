pkgname = "bluez-headers"
pkgver = "5.72"
pkgrel = 0
depends = ["!bluez-devel"]
pkgdesc = "Linux Bluetooth stack (header files)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://www.bluez.org"
source = f"$(KERNEL_SITE)/bluetooth/bluez-{pkgver}.tar.xz"
sha256 = "499d7fa345a996c1bb650f5c6749e1d929111fa6ece0be0e98687fee6124536e"


def do_install(self):
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
