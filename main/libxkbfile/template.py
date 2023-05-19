pkgname = "libxkbfile"
pkgver = "1.1.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libx11-devel"]
pkgdesc = "Xkbfile library from X.org"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/{pkgname}-{pkgver}.tar.gz"
sha256 = "d1a7e659bc7ae1aa1fc1ecced261c734df5ad5d86af1ef7a946be0e2d841e51d"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxkbfile-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
