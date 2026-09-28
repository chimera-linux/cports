pkgname = "libxxf86vm"
pkgver = "1.1.7"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xorgproto", "libxext-devel"]
pkgdesc = "XFree86-VidMode X extension library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXxf86vm-{pkgver}.tar.gz"
sha256 = "9a983e3cbb7a57905262291a17da962293c0645f99efd475e3c85264bfddc337"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxxf86vm-devel")
def _(self):
    return self.default_devel()
