pkgname = "libxau"
pkgver = "1.0.11"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto"]
pkgdesc = "Authorization Protocol for X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXau-{pkgver}.tar.gz"
sha256 = "3a321aaceb803577a4776a5efe78836eb095a9e44bbc7a465d29463e1a14f189"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxau-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
