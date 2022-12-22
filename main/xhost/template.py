pkgname = "xhost"
pkgver = "1.0.8"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel", "libxmu-devel"]
pkgdesc = "X server access control program"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "a2dc3c579e13674947395ef8ccc1b3763f89012a216c2cc6277096489aadc396"

def post_install(self):
    self.install_license("COPYING")

# FIXME visibility
hardening = ["!vis"]
