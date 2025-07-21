pkgname = "libxi"
pkgver = "1.8.2"
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
sha256 = "d0e0555e53d6e2114eabfa44226ba162d2708501a25e18d99cfb35c094c6c104"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxi-devel")
def _(self):
    return self.default_devel()
