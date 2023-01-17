pkgname = "libxkbfile"
pkgver = "1.1.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libx11-devel"]
pkgdesc = "Xkbfile library from X.org"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/{pkgname}-{pkgver}.tar.gz"
sha256 = "87faee6d4873c5631e8bb53e85134084b862185da682de8617f08ca18d82e216"
# unmarked api
hardening = ["!vis"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxkbfile-devel")
def _devel(self):
    return self.default_devel()
