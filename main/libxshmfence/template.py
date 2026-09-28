pkgname = "libxshmfence"
pkgver = "1.3.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-futex", "--with-shared-memory-dir=/dev/shm"]
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xorgproto", "linux-headers"]
pkgdesc = "X SyncFence synchronization primitive"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libxshmfence-{pkgver}.tar.gz"
sha256 = "6233ccd9fa80198835efc3039cdf8086ab2b218b17e77ebdb0a19913fcee58d3"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxshmfence-devel")
def _(self):
    return self.default_devel()
