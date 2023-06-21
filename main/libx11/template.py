pkgname = "libx11"
pkgver = "1.8.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-ipv6",
    "--enable-xlocaledir",
    "--enable-malloc0returnsnull",
    "--enable-static",
    "--without-xmlto",
]
configure_gen = []
hostmakedepends = ["pkgconf", "xorg-util-macros"]
makedepends = ["xorgproto", "xtrans", "libxcb-devel"]
pkgdesc = "Base X libraries from Xorg"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libX11-{pkgver}.tar.gz"
sha256 = "5ff0d26c94d82ebb94a944b9f1f55cd01b9713fd461fe93f62f3527ce14ad94e"
# FIXME int (_XkbReadGetIndicatorMapReply)
hardening = ["!int"]
# broken for now
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libx11-devel")
def _devel(self):
    return self.default_devel()
