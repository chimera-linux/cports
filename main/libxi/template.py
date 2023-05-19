pkgname = "libxi"
pkgver = "1.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf", "xmlto"]
makedepends = ["xorgproto", "libxfixes-devel", "libxext-devel"]
pkgdesc = "X Input extension library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXi-{pkgver}.tar.bz2"
sha256 = "2ed181446a61c7337576467870bc5336fc9e222a281122d96c4d39a3298bba00"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxi-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
