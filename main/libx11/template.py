pkgname = "libx11"
pkgver = "1.8.10"
pkgrel = 1
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
sha256 = "b7a1a90d881bb7b94df5cf31509e6b03f15c0972d3ac25ab0441f5fbc789650f"
# FIXME int (_XkbReadGetIndicatorMapReply)
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libx11-devel")
def _(self):
    return self.default_devel()
