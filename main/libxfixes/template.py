pkgname = "libxfixes"
pkgver = "6.0.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xorgproto", "libx11-devel"]
pkgdesc = "Xfixes library and extension of X RandR"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXfixes-{pkgver}.tar.gz"
sha256 = "041331b8e6e36038b3bf836785b6b175ec8515f964c9e4e3316b3bfed0f53ac7"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxfixes-devel")
def _(self):
    return self.default_devel()
