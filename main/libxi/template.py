pkgname = "libxi"
pkgver = "1.7.10"
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
sha256 = "36a30d8f6383a72e7ce060298b4b181fd298bc3a135c8e201b7ca847f5f81061"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxi-devel")
def _devel(self):
    return self.default_devel(man = True)
