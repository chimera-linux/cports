pkgname = "libxxf86vm"
pkgver = "1.1.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxext-devel"]
pkgdesc = "XFree86-VidMode X extension library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXxf86vm-{pkgver}.tar.gz"
sha256 = "d2b4b1ec4eb833efca9981f19ed1078a8a73eed0bb3ca5563b64527ae8021e52"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxxf86vm-devel")
def _(self):
    return self.default_devel()


configure_gen = []
