pkgname = "libxv"
pkgver = "1.0.11"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libx11-devel", "libxext-devel"]
pkgdesc = "Xv extension library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXv-{pkgver}.tar.bz2"
sha256 = "d26c13eac99ac4504c532e8e76a1c8e4bd526471eb8a0a4ff2a88db60cb0b088"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxv-static")
def _static(self):
    return self.default_static()

@subpackage("libxv-devel")
def _devel(self):
    return self.default_devel()
