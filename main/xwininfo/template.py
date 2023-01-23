pkgname = "xwininfo"
pkgver = "1.1.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel"]
pkgdesc = "Query information about X windows"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "7a405441dfc476666c744f5fcd1bc8a75abf8b5b1d85db7b88b370982365080e"
hardening = ["vis", "cfi"]

def post_install(self):
    self.install_license("COPYING")
