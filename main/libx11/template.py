pkgname = "libx11"
pkgver = "1.8.13"
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
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libX11-{pkgver}.tar.gz"
sha256 = "acf0e7cd7541110e6330ecb539441a2d53061f386ec7be6906dfde0de2598470"
# FIXME int (_XkbReadGetIndicatorMapReply)
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libx11-devel")
def _(self):
    return self.default_devel()
