pkgname = "libx11"
pkgver = "1.8.2"
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
sha256 = "f1bc56187bee0f830e1179ac5068ac93b78c51ace94eb27702ffb2efd116587b"
# broken for now
options = ["!cross"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libx11-devel")
def _devel(self):
    return self.default_devel()
