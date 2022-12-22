pkgname = "libice"
pkgver = "1.0.10"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "pkgconf", "automake", "libtool", "xorg-util-macros", "xtrans"
]
makedepends = ["xorgproto", "xtrans"]
pkgdesc = "Inter Client Exchange (ICE) library for X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libICE-{pkgver}.tar.bz2"
sha256 = "6f86dce12cf4bcaf5c37dddd8b1b64ed2ddf1ef7b218f22b9942595fb747c348"

def pre_configure(self):
    self.do("autoreconf", "-if")

def post_install(self):
    self.install_license("COPYING")

@subpackage("libice-devel")
def _devel(self):
    return self.default_devel()

# FIXME visibility
hardening = ["!vis"]
