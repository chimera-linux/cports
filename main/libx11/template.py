pkgname = "libx11"
pkgver = "1.8.1"
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
sha256 = "d52f0a7c02a45449f37b0831d99ff936d92eb4ce8b4c97dc17a63cea79ce5a76"
# broken for now
options = ["!cross"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libx11-devel")
def _devel(self):
    return self.default_devel()
