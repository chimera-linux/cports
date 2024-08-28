pkgname = "firmware-ipw2200"
pkgver = "3.1"
pkgrel = 0
pkgdesc = "Firmware for the Intel PRO/Wireless 2200BG wifi cards"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:ipw2200"
url = "http://ipw2200.sourceforge.net"
source = f"http://firmware.openbsd.org/firmware-dist/ipw2200-fw-{pkgver}.tgz"
sha256 = "c6818c11c18cc030d55ff83f64b2bad8feef485e7742f84f94a61d811a6258bd"
options = ["!strip", "foreignelf"]


def install(self):
    for f in self.cwd.glob("*.fw"):
        self.install_file(f, "usr/lib/firmware")

    self.install_license("LICENSE.ipw2200-fw")
