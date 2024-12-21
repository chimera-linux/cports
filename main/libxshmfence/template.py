pkgname = "libxshmfence"
pkgver = "1.3.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-futex", "--with-shared-memory-dir=/dev/shm"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "linux-headers"]
pkgdesc = "X SyncFence synchronization primitive"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libxshmfence-{pkgver}.tar.gz"
sha256 = "e93a85099604beb244ee756dcaf70e18b08701c1ca84c4de0126cd71bd6c8181"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxshmfence-devel")
def _(self):
    return self.default_devel()


configure_gen = []
