pkgname = "mtools"
pkgver = "4.0.44"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "texinfo"]
makedepends = ["acl-devel", "linux-headers"]
pkgdesc = "Utilities to access MS-DOS disks"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/mtools"
source = f"$(GNU_SITE)/mtools/mtools-{pkgver}.tar.bz2"
sha256 = "37dc4df022533c3d4b2ec1c78973c27c7e8b585374c2d46ab64c6a3db31eddb8"
# FIXME cfi
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_file("mtools.conf", "etc")
