pkgname = "xorg-util-macros"
pkgver = "1.20.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "X.org autotools macros"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://gitlab.freedesktop.org/xorg/util/macros"
source = f"$(XORG_SITE)/util/util-macros-{pkgver}.tar.gz"
sha256 = "8daf36913d551a90fd1013cb078401375dabae021cb4713b9b256a70f00eeb74"

def post_install(self):
    self.install_license("COPYING")

configure_gen = []
