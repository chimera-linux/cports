pkgname = "iw"
pkgver = "6.9"
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
url = "https://wireless.kernel.org/en/users/Documentation/iw"
source = f"https://www.kernel.org/pub/software/network/iw/iw-{pkgver}.tar.xz"
sha256 = "3f2db22ad41c675242b98ae3942dbf3112548c60a42ff739210f2de4e98e4894"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
