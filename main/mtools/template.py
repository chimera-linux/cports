pkgname = "mtools"
pkgver = "4.0.40"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["texinfo"]
makedepends = ["acl-devel", "linux-headers"]
pkgdesc = "Utilities to access MS-DOS disks"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/mtools"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "a22fca42354011dd2293a7f51f228b46ebbd802e7740b0975912afecb79d5df4"

def post_install(self):
    self.install_file("mtools.conf", "etc")
