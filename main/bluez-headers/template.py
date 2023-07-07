pkgname = "bluez-headers"
pkgver = "5.68"
pkgrel = 0
depends = ["!bluez-devel"]
pkgdesc = "Linux Bluetooth stack (header files)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://www.bluez.org"
source = f"$(KERNEL_SITE)/bluetooth/bluez-{pkgver}.tar.xz"
sha256 = "fc505e6445cb579a55cacee6821fe70d633921522043d322b696de0a175ff933"


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
