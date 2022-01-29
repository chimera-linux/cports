pkgname = "xmodmap"
pkgver = "1.0.10"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel"]
pkgdesc = "Modify X keymaps and pointer button mappings"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "473f0941d7439d501bb895ff358832b936ec34c749b9704c37a15e11c318487c"

def post_install(self):
    self.install_license("COPYING")
