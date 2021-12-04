pkgname = "font-util"
pkgver = "1.3.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "bdftopcf"]
# not strictly dependencies per se, just to drag them in
depends = ["font-alias", "fontconfig", "mkfontscale"]
pkgdesc = "X.org font utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/font/{pkgname}-{pkgver}.tar.bz2"
sha256 = "3ad880444123ac06a7238546fa38a2a6ad7f7e0cc3614de7e103863616522282"

def post_install(self):
    self.install_license("COPYING")

@subpackage("font-util-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel()
