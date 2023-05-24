pkgname = "xauth"
pkgver = "1.1.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xtrans", "libxau-devel", "libxext-devel", "libxmu-devel"]
pkgdesc = "X authentication utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.gz"
sha256 = "84d27a1023d8da524c134f424b312e53cb96e08871f96868aa20316bfcbbc054"
hardening = ["vis", "cfi"]
# needs cmdtest
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
