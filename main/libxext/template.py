pkgname = "libxext"
pkgver = "1.3.7"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "xorg-util-macros",
]
makedepends = ["xorgproto", "libx11-devel"]
pkgdesc = "X extension library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXext-{pkgver}.tar.xz"
sha256 = "6c643c7035cdacf67afd68f25d01b90ef889d546c9fcd7c0adf7c2cf91e3a32d"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxext-devel")
def _(self):
    return self.default_devel()
