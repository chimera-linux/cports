pkgname = "mac-fdisk"
pkgver = "0.1"
pkgrel = 0
build_style = "makefile"
makedepends = ["linux-headers"]
pkgdesc = "Apple Partition Map utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://packages.debian.org/sid/mac-fdisk"
source = f"http://deb.debian.org/debian/pool/main/m/mac-fdisk/mac-fdisk_{pkgver}.orig.tar.gz"
sha256 = "7059fc4ba41ca2ef857e1092e9c56e910f27693d407b5c3d78f7102ad0c56a66"
# no tests
options = ["!check"]


tool_flags = {"CFLAGS": ["-D_GNU_SOURCE", "-D_LARGEFILE64_SOURCE"]}


def install(self):
    self.install_bin("pdisk", name="mac-fdisk")
    self.install_bin("fdisk", name="pmac-fdisk")

    self.install_man("mac-fdisk.8.in", name="mac-fdisk", cat=8)
    self.install_man("pmac-fdisk.8.in", name="pmac-fdisk", cat=8)

    self.install_file("README", "usr/share/doc/mac-fdisk")
    self.install_file("HISTORY", "usr/share/doc/mac-fdisk")
