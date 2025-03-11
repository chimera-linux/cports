pkgname = "mtools"
pkgver = "4.0.48"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "texinfo"]
makedepends = ["acl-devel", "linux-headers"]
pkgdesc = "Utilities to access MS-DOS disks"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/mtools"
source = f"$(GNU_SITE)/mtools/mtools-{pkgver}.tar.bz2"
sha256 = "03c29aac8735dd7154a989fbc29eaf2b506121ae1c3a35cd0bf2a02e94d271a9"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_file("mtools.conf", "etc")
