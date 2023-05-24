pkgname = "libxext"
pkgver = "1.3.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libx11-devel"]
pkgdesc = "X extension library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXext-{pkgver}.tar.gz"
sha256 = "1a3dcda154f803be0285b46c9338515804b874b5ccc7a2b769ab7fd76f1035bd"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxext-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
