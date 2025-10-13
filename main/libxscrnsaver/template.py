pkgname = "libxscrnsaver"
pkgver = "1.2.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xorgproto", "libx11-devel", "libxext-devel"]
pkgdesc = "X Screensaver Library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXScrnSaver-{pkgver}.tar.gz"
sha256 = "356f45ae365403b5500702b6b7c6e708d02a5b0ada0e5a6c859db677e41fdb00"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxscrnsaver-devel")
def _(self):
    return self.default_devel()
