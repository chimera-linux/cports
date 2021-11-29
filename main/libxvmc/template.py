pkgname = "libxvmc"
pkgver = "1.0.12"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libx11-devel", "libxext-devel", "libxv-devel"]
pkgdesc = "XvMC extension library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXvMC-{pkgver}.tar.bz2"
sha256 = "6b3da7977b3f7eaf4f0ac6470ab1e562298d82c4e79077765787963ab7966dcd"
options = ["lto"]

def post_install(self):
    self.install_license("COPYING")
    # in xorgproto
    self.rm(self.destdir / "usr/include/X11/extensions/vldXvMC.h")

@subpackage("libxvmc-static")
def _static(self):
    return self.default_static()

@subpackage("libxvmc-devel")
def _devel(self):
    return self.default_devel(man = True, extra = ["usr/share/doc"])
