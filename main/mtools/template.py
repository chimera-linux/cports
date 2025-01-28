pkgname = "mtools"
pkgver = "4.0.47"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "texinfo"]
makedepends = ["acl-devel", "linux-headers"]
pkgdesc = "Utilities to access MS-DOS disks"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/mtools"
source = f"$(GNU_SITE)/mtools/mtools-{pkgver}.tar.bz2"
sha256 = "31aa06078cc3f50591b95e71a909c56dd179d87e9cbdc07bf435e595bd7cc7ff"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_file("mtools.conf", "etc")
