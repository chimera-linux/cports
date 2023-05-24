pkgname = "iw"
pkgver = "5.19"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_install_args = ["SBINDIR=/usr/bin"]
make_use_env = True
hostmakedepends = ["gmake", "gsed", "pkgconf", "libnl-devel"]
makedepends = ["libnl-devel", "linux-headers"]
pkgdesc = "Utility for nl80211 based CLI configuration of wireless devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "http://wireless.kernel.org/en/users/Documentation/iw"
source = f"http://www.kernel.org/pub/software/network/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "f167bbe947dd53bb9ebc0c1dcef5db6ad73ac1d6084f2c6f9376c5c360cc4d4e"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
