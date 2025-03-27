pkgname = "libx11"
pkgver = "1.8.12"
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
sha256 = "220fbcf54b6e4d8dc40076ff4ab87954358019982490b33c7802190b62d89ce1"
# FIXME int (_XkbReadGetIndicatorMapReply)
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libx11-devel")
def _(self):
    return self.default_devel()
