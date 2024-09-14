pkgname = "xvinfo"
pkgver = "1.1.5"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libxv-devel"]
pkgdesc = "X video capabilities query utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xvinfo-{pkgver}.tar.gz"
sha256 = "76fdc89a4e4207d0069ae3e511b4e30a60fcf86b630d01ef56d32ba5856e76c4"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
