pkgname = "xset"
pkgver = "1.2.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = [
    "libxmu-devel", "libxext-devel", "libxxf86misc-devel",
    "libxfontcache-devel"
]
pkgdesc = "X11 user preferences utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "e4fd95280df52a88e9b0abc1fee11dcf0f34fc24041b9f45a247e52df941c957"
# needs cmdtest
options = ["!check"]

def post_install(self):
    self.install_license("COPYING")
