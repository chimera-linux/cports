pkgname = "xeyes"
pkgver = "1.3.0"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "xorg-util-macros"]
makedepends = ["libxmu-devel", "libxt-devel", "libxrender-devel", "libxi-devel"]
pkgdesc = "Follow the mouse"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xeyes-{pkgver}.tar.gz"
sha256 = "e2f0ab2fd48d12444e42e537e235dc6141bb1750f2206140fe380fda6d7e1196"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
