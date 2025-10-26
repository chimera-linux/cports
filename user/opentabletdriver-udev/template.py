pkgname = "opentabletdriver-udev"
pkgver = "0.6.6.2"
pkgrel = 0
hostmakedepends = ["bash", "jq"]
pkgdesc = "Udev rules for OpenTabletDriver"
license = "LGPL-3.0-or-later"
url = "https://opentabletdriver.net"
source = f"https://github.com/OpenTabletDriver/OpenTabletDriver/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1602f3291bad333be56671933e5ba6fb17144432729c10b2a0b40626e8c9dd28"


def build(self):
    with open(f"{self.cwd}/99-opentabletdriver.rules", "w") as o:
        self.do("./generate-rules.sh", stdout=o)


def install(self):
    self.install_file("99-opentabletdriver.rules", "usr/lib/udev/rules.d")
    self.install_file(
        "eng/linux/Generic/usr/lib/modprobe.d/99-opentabletdriver.conf",
        "usr/lib/modprobe.d",
    )
