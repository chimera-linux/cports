pkgname = "iw"
pkgver = "6.17"
pkgrel = 0
build_style = "makefile"
make_install_args = ["SBINDIR=/usr/bin"]
make_use_env = True
hostmakedepends = ["gsed", "pkgconf", "libnl-devel"]
makedepends = ["libnl-devel", "linux-headers"]
pkgdesc = "Utility for nl80211 based CLI configuration of wireless devices"
license = "ISC"
url = "https://wireless.kernel.org/en/users/Documentation/iw"
source = f"https://www.kernel.org/pub/software/network/iw/iw-{pkgver}.tar.xz"
sha256 = "7d182e498289ab39b257da6780d562e415377107f50358ee5b55b8cfe40b1e33"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
