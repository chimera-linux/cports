pkgname = "iw"
pkgver = "5.9"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_install_args = ["SBINDIR=/usr/bin"]
make_use_env = True
hostmakedepends = ["gmake", "gsed", "pkgconf", "libnl3-devel"]
makedepends = ["libnl3-devel", "linux-headers"]
pkgdesc = "Utility for nl80211 based CLI configuration of wireless devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "http://wireless.kernel.org/en/users/Documentation/iw"
source = f"http://www.kernel.org/pub/software/network/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "293a07109aeb7e36267cf59e3ce52857e9ffae3a6666eb8ac77894b1839fe1f2"

def post_install(self):
    self.install_license("COPYING")
