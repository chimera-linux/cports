pkgname = "mtools"
pkgver = "4.0.42"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["texinfo"]
makedepends = ["acl-devel", "linux-headers"]
pkgdesc = "Utilities to access MS-DOS disks"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/mtools"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "64bfdfde4d82af6b22f3c1c72c3e231cbb618f4c2309cc46f54d16d5502ccf15"
# FIXME cfi
hardening = ["!cfi"]

def post_install(self):
    self.install_file("mtools.conf", "etc")
