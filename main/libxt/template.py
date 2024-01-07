pkgname = "libxt"
pkgver = "1.3.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libsm-devel", "libx11-devel"]
pkgdesc = "X Toolkit Intrinsics library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXt-{pkgver}.tar.gz"
sha256 = "de4a80c4cc7785b9620e572de71026805f68e85a2bf16c386009ef0e50be3f77"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxt-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
