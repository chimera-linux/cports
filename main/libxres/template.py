pkgname = "libxres"
pkgver = "1.2.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xorgproto", "libxext-devel"]
pkgdesc = "X extension library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXres-{pkgver}.tar.gz"
sha256 = "e1ee4845aa6a59e6ba7145422279ffc7da521b4d3dd302c0b1febdf45d06d093"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxres-devel")
def _(self):
    return self.default_devel()
