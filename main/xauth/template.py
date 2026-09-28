pkgname = "xauth"
pkgver = "1.1.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["xtrans", "libxau-devel", "libxext-devel", "libxmu-devel"]
pkgdesc = "X authentication utility"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xauth-{pkgver}.tar.gz"
sha256 = "c1149ecf010d7cf717952325c54f3cd78e75b435758b6d09172b0445be477537"
hardening = ["vis", "cfi"]
# needs cmdtest
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
