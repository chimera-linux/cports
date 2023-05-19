pkgname = "mtools"
pkgver = "4.0.43"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["texinfo"]
makedepends = ["acl-devel", "linux-headers"]
pkgdesc = "Utilities to access MS-DOS disks"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/mtools"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "541e179665dc4e272b9602f2074243591a157da89cc47064da8c5829dbd2b339"
# FIXME cfi
hardening = ["vis", "!cfi"]

def post_install(self):
    self.install_file("mtools.conf", "etc")

configure_gen = []
