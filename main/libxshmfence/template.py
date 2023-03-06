pkgname = "libxshmfence"
pkgver = "1.3.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-futex", "--with-shared-memory-dir=/dev/shm"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "linux-headers"]
pkgdesc = "X SyncFence synchronization primitive"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/{pkgname}-{pkgver}.tar.gz"
sha256 = "033fdcb4f5efa95b6ca3979e5ba190948e73c50cd9b0ea0a6a45e934c93c3969"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxshmfence-devel")
def _devel(self):
    return self.default_devel()
