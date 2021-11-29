pkgname = "libxft"
pkgver = "2.3.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = [
    "xorgproto", "libxrender-devel", "freetype-devel", "fontconfig-devel"
]
pkgdesc = "X font library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXft-{pkgver}.tar.bz2"
sha256 = "57dedaab20914002146bdae0cb0c769ba3f75214c4c91bd2613d6ef79fc9abdd"
options = ["lto"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxft-static")
def _static(self):
    return self.default_static()

@subpackage("libxft-devel")
def _devel(self):
    return self.default_devel(man = True)
