pkgname = "libx11"
pkgver = "1.8.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-ipv6",
    "--enable-xlocaledir",
    "--enable-malloc0returnsnull",
    "--enable-static",
    "--without-xmlto",
]
hostmakedepends = ["pkgconf", "xorg-util-macros"]
makedepends = ["xorgproto", "xtrans", "libxcb-devel"]
pkgdesc = "Base X libraries from Xorg"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libX11-{pkgver}.tar.gz"
sha256 = "efd3a3a43c1f177edc2c205bedb0719b6648203595e54c0b83a32576aeaca7cd"
# FIXME int (_XkbReadGetIndicatorMapReply)
hardening = ["!int"]
# broken for now
options = ["!cross"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libx11-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
