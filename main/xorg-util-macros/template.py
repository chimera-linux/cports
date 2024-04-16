pkgname = "xorg-util-macros"
pkgver = "1.20.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf"]
pkgdesc = "X.org autotools macros"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://gitlab.freedesktop.org/xorg/util/macros"
source = f"$(XORG_SITE)/util/util-macros-{pkgver}.tar.gz"
sha256 = "b373f72887b1394ce2193180a60cb0d1fb8b17bc96ddd770cfd7a808cb489a15"


def post_install(self):
    self.install_license("COPYING")
