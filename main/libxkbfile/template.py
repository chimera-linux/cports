pkgname = "libxkbfile"
pkgver = "1.1.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libx11-devel"]
pkgdesc = "Xkbfile library from X.org"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/{pkgname}-{pkgver}.tar.bz2"
sha256 = "758dbdaa20add2db4902df0b1b7c936564b7376c02a0acd1f2a331bd334b38c7"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxkbfile-static")
def _static(self):
    return self.default_static()

@subpackage("libxkbfile-devel")
def _devel(self):
    return self.default_devel()
