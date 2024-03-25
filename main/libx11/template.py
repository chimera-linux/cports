pkgname = "libx11"
pkgver = "1.8.8"
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
sha256 = "26997a2bc48c03df7d670f8a4ee961d1d6b039bf947475e5fec6b7635b4efe72"
# FIXME int (_XkbReadGetIndicatorMapReply)
hardening = ["!int"]
# broken for now
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libx11-devel")
def _devel(self):
    return self.default_devel()
