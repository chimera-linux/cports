pkgname = "font-util"
pkgver = "1.4.0"
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
sha256 = "30b90fe52347916be9b08f95f717f17c9c1f58bef8cabb49014d0fdd2b0df643"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("font-util-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel()


configure_gen = []
