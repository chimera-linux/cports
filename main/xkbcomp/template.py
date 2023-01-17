pkgname = "xkbcomp"
pkgver = "1.4.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "bison"]
makedepends = ["libx11-devel", "libxkbfile-devel"]
pkgdesc = "XKBD keymap compiler"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "6851086c4244b6fd0cc562880d8ff193fb2bbf1e141c73632e10731b31d4b05e"

def post_install(self):
    self.install_license("COPYING")
