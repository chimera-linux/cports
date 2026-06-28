pkgname = "libxi"
pkgver = "1.8.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "xmlto",
    "xorg-util-macros",
]
makedepends = ["xorgproto", "libxfixes-devel", "libxext-devel"]
pkgdesc = "X Input extension library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXi-{pkgver}.tar.xz"
sha256 = "7ad60056f01af4f786cfe93b3a7707447711626fc8da2637bec71a90409babe5"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxi-devel")
def _(self):
    return self.default_devel()
