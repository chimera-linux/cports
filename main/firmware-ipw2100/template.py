pkgname = "firmware-ipw2100"
pkgver = "1.3"
pkgrel = 0
pkgdesc = "Firmware for the Intel PRO/Wireless 2100 wifi cards"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:ipw2100"
url = "http://ipw2100.sourceforge.net"
source = f"http://firmware.openbsd.org/firmware-dist/ipw2100-fw-{pkgver}.tgz"
sha256 = "e1107c455e48d324a616b47a622593bc8413dcce72026f72731c0b03dae3a7a2"
options = ["!strip", "foreignelf"]


def install(self):
    for f in self.cwd.glob("*.fw"):
        self.install_file(f, "usr/lib/firmware")

    self.install_license("LICENSE")
