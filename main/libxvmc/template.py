pkgname = "libxvmc"
pkgver = "1.0.13"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libx11-devel", "libxext-devel", "libxv-devel"]
pkgdesc = "XvMC extension library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXvMC-{pkgver}.tar.gz"
sha256 = "e630b4373af8c67a7c8f07ebe626a1269a613d262d1f737b57231a06f7c34b4e"


def post_install(self):
    self.install_license("COPYING")
    # in xorgproto
    self.rm(self.destdir / "usr/include/X11/extensions/vldXvMC.h")


@subpackage("libxvmc-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/doc"])


configure_gen = []
