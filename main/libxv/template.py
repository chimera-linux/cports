pkgname = "libxv"
pkgver = "1.0.12"
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
sha256 = "ce706619a970a580a0e35e9b5c98bdd2af243ac6494c65f44608a89a86100126"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxv-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
