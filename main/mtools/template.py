pkgname = "mtools"
pkgver = "4.0.46"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "texinfo"]
makedepends = ["acl-devel", "linux-headers"]
pkgdesc = "Utilities to access MS-DOS disks"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/mtools"
source = f"$(GNU_SITE)/mtools/mtools-{pkgver}.tar.bz2"
sha256 = "9aad8dd859f88fb7787924ec47590192d3abf7bad6c840509c854290d6bc16c0"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_file("mtools.conf", "etc")
