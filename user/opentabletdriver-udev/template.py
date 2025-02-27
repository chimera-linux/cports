pkgname = "opentabletdriver-udev"
pkgver = "0.6.5.1"
pkgrel = 0
hostmakedepends = ["bash", "jq"]
pkgdesc = "Udev rules for OpenTabletDriver"
license = "LGPL-3.0-or-later"
url = "https://opentabletdriver.net"
source = f"https://github.com/OpenTabletDriver/OpenTabletDriver/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "682cea127a583b9e4a2fceaf8ec92557502a25ce7d34b18b085ba790c911f0cb"


def build(self):
    with open(f"{self.cwd}/99-opentabletdriver.rules", "w") as o:
        self.do("./generate-rules.sh", stdout=o)


def install(self):
    self.install_file("99-opentabletdriver.rules", "usr/lib/udev/rules.d")
    self.install_file(
        "eng/linux/Generic/usr/lib/modprobe.d/99-opentabletdriver.conf",
        "usr/lib/modprobe.d",
    )
