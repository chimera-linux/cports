pkgname = "xorg-util-macros"
pkgver = "1.19.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "X.org autotools macros"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://gitlab.freedesktop.org/xorg/util/macros"
source = f"$(XORG_SITE)/util/util-macros-{pkgver}.tar.bz2"
sha256 = "0f812e6e9d2786ba8f54b960ee563c0663ddbe2434bf24ff193f5feab1f31971"

def post_install(self):
    self.install_license("COPYING")

# FIXME visibility
hardening = ["!vis"]
