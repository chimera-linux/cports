pkgname = "font-util"
pkgver = "1.3.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "bdftopcf"]
# not strictly dependencies per se, just to drag them in
depends = ["font-alias", "fontconfig", "mkfontscale"]
pkgdesc = "X.org font utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/font/{pkgname}-{pkgver}.tar.gz"
sha256 = "2094dd4a1ca63a61deb101d2dc618682d6e287cdbe09679502223ac445d277dc"

def post_install(self):
    self.install_license("COPYING")

@subpackage("font-util-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel()

# FIXME visibility
hardening = ["!vis"]
