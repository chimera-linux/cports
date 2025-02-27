pkgname = "libxrender"
pkgver = "0.9.12"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xorgproto", "libxext-devel"]
pkgdesc = "X Render library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXrender-{pkgver}.tar.gz"
sha256 = "0fff64125819c02d1102b6236f3d7d861a07b5216d8eea336c3811d31494ecf7"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxrender-devel")
def _(self):
    return self.default_devel()
