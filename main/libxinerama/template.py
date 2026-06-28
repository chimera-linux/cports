pkgname = "libxinerama"
pkgver = "1.1.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xorgproto", "libxext-devel"]
pkgdesc = "PanoramiX extension library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXinerama-{pkgver}.tar.gz"
sha256 = "c74ee3d05e473671bf86285e2dece345485200bb042bea1540b1e30ff3f74bae"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxinerama-devel")
def _(self):
    return self.default_devel()
