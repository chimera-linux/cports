pkgname = "libxxf86misc"
pkgver = "1.0.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xorgproto", "libxext-devel", "libx11-devel"]
pkgdesc = "XFree86-Misc X extension library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXxf86misc-{pkgver}.tar.bz2"
sha256 = "a89c03e2b0f16239d67a2031b9003f31b5a686106bbdb3c797fb88ae472af380"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxxf86misc-devel")
def _(self):
    return self.default_devel()
