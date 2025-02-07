pkgname = "libx11"
pkgver = "1.8.11"
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
sha256 = "17a37d1597354a1d8040196f1cdac54240c78c0bd1a1a95e97cc23215cf0b734"
# FIXME int (_XkbReadGetIndicatorMapReply)
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libx11-devel")
def _(self):
    return self.default_devel()
