pkgname = "libxrandr"
pkgver = "1.5.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["automake", "libtool", "pkgconf", "xorg-util-macros"]
makedepends = ["xorgproto", "libxext-devel", "libxrender-devel"]
pkgdesc = "X RandR Library from X.org"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXrandr-{pkgver}.tar.gz"
sha256 = "c72c94dc3373512ceb67f578952c5d10915b38cc9ebb0fd176a49857b8048e22"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxrandr-devel")
def _devel(self):
    return self.default_devel()
