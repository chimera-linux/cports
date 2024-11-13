pkgname = "xorg-util-macros"
pkgver = "1.20.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf"]
pkgdesc = "X.org autotools macros"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://gitlab.freedesktop.org/xorg/util/macros"
source = f"$(XORG_SITE)/util/util-macros-{pkgver}.tar.gz"
sha256 = "f642f8964d81acdf06653fdf9dbc210c43ce4bd308bd644a8d573148d0ced76b"


def post_install(self):
    self.install_license("COPYING")
