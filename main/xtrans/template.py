pkgname = "xtrans"
pkgver = "1.5.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "xorg-util-macros"]
pkgdesc = "Network API translation layer to insulate X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/xtrans-{pkgver}.tar.gz"
sha256 = "8327cd270f3b91c66de9f9fd9069cebd77d0827c60dcde30ff8d9bec9224d8c5"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
