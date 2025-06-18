pkgname = "mtools"
pkgver = "4.0.49"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "texinfo"]
makedepends = ["acl-devel", "linux-headers"]
pkgdesc = "Utilities to access MS-DOS disks"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/mtools"
source = f"$(GNU_SITE)/mtools/mtools-{pkgver}.tar.bz2"
sha256 = "6fe5193583d6e7c59da75e63d7234f76c0b07caf33b103894f46f66a871ffc9f"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_file("mtools.conf", "etc")
