pkgname = "libx11"
pkgver = "1.7.5"
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
sha256 = "78992abcd2bfdebe657699203ad8914e7ae77025175460e04a1045387192a978"
# broken for now
options = ["!cross"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libx11-devel")
def _devel(self):
    return self.default_devel()
