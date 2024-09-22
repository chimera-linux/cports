pkgname = "opentabletdriver-udev"
pkgver = "0.6.4.0"
pkgrel = 0
hostmakedepends = ["bash", "jq"]
pkgdesc = "Udev rules for OpenTabletDriver"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "LGPL-3.0-or-later"
url = "https://opentabletdriver.net"
source = f"https://github.com/OpenTabletDriver/OpenTabletDriver/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1ad04f4a32b54b9b62bd944b0196abb6613873b19c269abcc9f9e94c1dc3027f"


def build(self):
    with open(f"{self.cwd}/99-opentabletdriver.rules", "w") as o:
        self.do("./generate-rules.sh", stdout=o)


def install(self):
    self.install_file("99-opentabletdriver.rules", "usr/lib/udev/rules.d")
    self.install_file(
        "eng/linux/Generic/usr/lib/modprobe.d/99-opentabletdriver.conf",
        "usr/lib/modprobe.d",
    )
