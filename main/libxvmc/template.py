pkgname = "libxvmc"
pkgver = "1.0.14"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["xorgproto", "libx11-devel", "libxext-devel", "libxv-devel"]
pkgdesc = "XvMC extension library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXvMC-{pkgver}.tar.xz"
sha256 = "e4be9eb6b6bafdbbf81f47f7163047215376e45e2dc786d0ea6181c930725ed9"


def post_install(self):
    self.install_license("COPYING")
    # in xorgproto
    self.uninstall("usr/include/X11/extensions/vldXvMC.h")


@subpackage("libxvmc-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/doc"])
