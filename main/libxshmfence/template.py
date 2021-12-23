pkgname = "libxshmfence"
pkgver = "1.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-shared-memory-dir=/dev/shm"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto"]
pkgdesc = "X SyncFence synchronization primitive"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libxshmfence-{pkgver}.tar.bz2"
sha256 = "b884300d26a14961a076fbebc762a39831cb75f92bed5ccf9836345b459220c7"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxshmfence-static")
def _static(self):
    return self.default_static()

@subpackage("libxshmfence-devel")
def _devel(self):
    return self.default_devel()
