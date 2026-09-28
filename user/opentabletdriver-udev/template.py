pkgname = "opentabletdriver-udev"
pkgver = "0.6.7"
pkgrel = 0
hostmakedepends = ["bash", "jq"]
pkgdesc = "Udev rules for OpenTabletDriver"
license = "LGPL-3.0-or-later"
url = "https://opentabletdriver.net"
source = f"https://github.com/OpenTabletDriver/OpenTabletDriver/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "95e8fe646ccfcee97da5477f2432ce3265ec6c0c5356a23b1b2f41a0b738796f"


def build(self):
    with open(f"{self.cwd}/99-opentabletdriver.rules", "w") as o:
        self.do("./generate-rules.sh", stdout=o)


def install(self):
    self.install_file("99-opentabletdriver.rules", "usr/lib/udev/rules.d")
    self.install_file(
        "eng/bash/Generic/usr/lib/modprobe.d/99-opentabletdriver.conf",
        "usr/lib/modprobe.d",
    )
