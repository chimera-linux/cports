pkgname = "font-util"
pkgver = "1.4.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "bdftopcf",
    "pkgconf",
    "xorg-util-macros",
]
# not strictly dependencies per se, just to drag them in
depends = ["font-alias", "fontconfig", "mkfontscale"]
pkgdesc = "X.org font utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/font/{pkgname}-{pkgver}.tar.gz"
sha256 = "f029ae80cdd75d89bee7f7af61c21e07982adfb9f72344a158b99f91f77ef5ed"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("font-util-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel()
