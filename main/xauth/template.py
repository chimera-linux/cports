pkgname = "xauth"
pkgver = "1.1.3"
pkgrel = 2
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["xtrans", "libxau-devel", "libxext-devel", "libxmu-devel"]
pkgdesc = "X authentication utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xauth-{pkgver}.tar.gz"
sha256 = "88c288e0a30bf071631118644f5232cae3a79713a7c82dd31a236e8e2c6fca15"
hardening = ["vis", "cfi"]
# needs cmdtest
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
