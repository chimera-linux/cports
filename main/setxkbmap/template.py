pkgname = "setxkbmap"
pkgver = "1.3.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel", "libxkbfile-devel"]
pkgdesc = "Sets the X keyboard layout"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "8ff27486442725e50b02d7049152f51d125ecad71b7ce503cfa09d5d8ceeb9f5"

def post_install(self):
    self.install_license("COPYING")
