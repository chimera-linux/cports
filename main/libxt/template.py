pkgname = "libxt"
pkgver = "1.3.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xorgproto", "libsm-devel", "libx11-devel"]
pkgdesc = "X Toolkit Intrinsics library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXt-{pkgver}.tar.xz"
sha256 = "e0a774b33324f4d4c05b199ea45050f87206586d81655f8bef4dba434d931288"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxt-devel")
def _(self):
    return self.default_devel()
