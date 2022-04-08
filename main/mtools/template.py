pkgname = "mtools"
pkgver = "4.0.38"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["texinfo"]
makedepends = ["acl-devel", "linux-headers"]
pkgdesc = "Utilities to access MS-DOS disks"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/mtools"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "7b94485f486e7df08cca68b00a164a13cd38f4c63cb8684d188759ee7bc5e729"

def post_install(self):
    self.install_file("mtools.conf", "etc")
