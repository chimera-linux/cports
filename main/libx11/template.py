pkgname = "libx11"
pkgver = "1.8.7"
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
sha256 = "793ebebf569f12c864b77401798d38814b51790fce206e01a431e5feb982e20b"
# FIXME int (_XkbReadGetIndicatorMapReply)
hardening = ["!int"]
# broken for now
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libx11-devel")
def _devel(self):
    return self.default_devel()
