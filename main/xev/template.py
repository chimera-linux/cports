pkgname = "xev"
pkgver = "1.2.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libxrandr-devel"]
pkgdesc = "Display X events"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.gz"
sha256 = "a948974ede621a8402ed9ea64f1ec83992285aa4fbb9d40b52985156c61a358a"
hardening = ["vis", "cfi"]

def post_install(self):
    self.install_license("COPYING")

configure_gen = []
