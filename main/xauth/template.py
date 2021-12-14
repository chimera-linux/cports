pkgname = "xauth"
pkgver = "1.1.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xtrans", "libxau-devel", "libxext-devel", "libxmu-devel"]
pkgdesc = "X authentication utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "164ea0a29137b284a47b886ef2affcb0a74733bf3aad04f9b106b1a6c82ebd92"
# needs cmdtest
options = ["!check"]

def post_install(self):
    self.install_license("COPYING")
