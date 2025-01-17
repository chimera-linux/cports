pkgname = "opentabletdriver-udev"
pkgver = "0.6.5.0"
pkgrel = 0
hostmakedepends = ["bash", "jq"]
pkgdesc = "Udev rules for OpenTabletDriver"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://opentabletdriver.net"
source = f"https://github.com/OpenTabletDriver/OpenTabletDriver/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "139f8c8cc28c6687a452bec4e642f4e8523ac1ef34d019c848133fcfdb22d847"


def build(self):
    with open(f"{self.cwd}/99-opentabletdriver.rules", "w") as o:
        self.do("./generate-rules.sh", stdout=o)


def install(self):
    self.install_file("99-opentabletdriver.rules", "usr/lib/udev/rules.d")
    self.install_file(
        "eng/linux/Generic/usr/lib/modprobe.d/99-opentabletdriver.conf",
        "usr/lib/modprobe.d",
    )
