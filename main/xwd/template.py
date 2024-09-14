pkgname = "xwd"
pkgver = "1.0.9"
pkgrel = 2
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool", "xorg-util-macros"]
makedepends = ["libx11-devel", "libxkbfile-devel"]
pkgdesc = "Dump an image of an X window"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xwd-{pkgver}.tar.gz"
sha256 = "5fa984e1f7799a7e23ea4e795b3b61483e28df6d0284bae11062f6256c30a9c1"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")
