pkgname = "libxpm"
pkgver = "3.5.13"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "gettext-tiny"]
makedepends = ["xorgproto", "libsm-devel", "libxext-devel", "libxt-devel"]
pkgdesc = "X PixMap library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXpm-{pkgver}.tar.bz2"
sha256 = "9cd1da57588b6cb71450eff2273ef6b657537a9ac4d02d0014228845b935ac25"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxpm-static")
def _static(self):
    return self.default_static()

@subpackage("libxpm-devel")
def _devel(self):
    return self.default_devel(man = True)
