pkgname = "iw"
pkgver = "5.16"
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
sha256 = "4c44e42762f903f9094ba5a598998c800a97a62afd6fd31ec1e0a799e308659c"
options = ["lto"]

def post_install(self):
    self.install_license("COPYING")
