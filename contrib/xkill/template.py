pkgname = "xkill"
pkgver = "1.0.6"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel", "libxmu-devel"]
pkgdesc = "Kill an X client by its X resource"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xkill-{pkgver}.tar.gz"
sha256 = "3b35a2f4b67dda1e98b6541488cd7f7343eb6e3dbe613aeff3d5a5a4c4c64b58"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
