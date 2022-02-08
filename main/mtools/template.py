pkgname = "mtools"
pkgver = "4.0.37"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["texinfo"]
makedepends = ["acl-devel", "linux-headers"]
pkgdesc = "Utilities to access MS-DOS disks"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/mtools"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "799b197e23e47b61259628810b27790efb7a1fe36037ef1da8a27b0ae4fa8342"

def post_install(self):
    self.install_file("mtools.conf", "etc")
