pkgname = "libxau"
pkgver = "1.0.12"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto"]
pkgdesc = "Authorization Protocol for X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXau-{pkgver}.tar.gz"
sha256 = "2402dd938da4d0a332349ab3d3586606175e19cb32cb9fe013c19f1dc922dcee"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxau-devel")
def _(self):
    return self.default_devel()


configure_gen = []
