pkgname = "firmware-zd1211"
pkgver = "1.5"
pkgrel = 0
pkgdesc = "Firmware for the Zydas 1211 wifi cards"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://zd1211.wiki.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/zd1211/zd1211-firmware-{pkgver}.tar.bz2"
sha256 = "f11d3810d7f72833997f634584a586dcced71a353f965abf81062ec431d02b12"
options = ["!strip", "foreignelf"]


def install(self):
    for f in self.cwd.glob("zd1211*"):
        self.install_file(f, "usr/lib/firmware/zd1211")
