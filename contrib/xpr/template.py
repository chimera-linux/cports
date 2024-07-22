pkgname = "xpr"
pkgver = "1.2.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["libx11-devel", "libxmu-devel"]
pkgdesc = "Print an X window dump"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xpr-{pkgver}.tar.gz"
sha256 = "4c37dd062c8f61618ed5fad7be907d7f9b219c2c91aa9a312f4ff4cc3494c476"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
