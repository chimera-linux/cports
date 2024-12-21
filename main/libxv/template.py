pkgname = "libxv"
pkgver = "1.0.13"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libx11-devel", "libxext-devel"]
pkgdesc = "Xv extension library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXv-{pkgver}.tar.gz"
sha256 = "9a0c31392b8968a4f29a0ad9c51e7ce225bcec3c4cbab9f2a241f921776b2991"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxv-devel")
def _(self):
    return self.default_devel()


configure_gen = []
