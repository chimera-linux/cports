pkgname = "setxkbmap"
pkgver = "1.3.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel", "libxkbfile-devel", "libxrandr-devel"]
pkgdesc = "Sets the X keyboard layout"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.gz"
sha256 = "51ba28edf93a464a7444b53b154fd5e93dedd1e9bbcc85b636f4cf56986c4842"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
