pkgname = "libsm"
pkgver = "1.2.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf", "xorg-util-macros"]
makedepends = ["libice-devel", "util-linux-uuid-devel", "xtrans"]
pkgdesc = "X session management library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libSM-{pkgver}.tar.gz"
sha256 = "a11c3d23b60dce0c13256a8ce9478c1ea330719c0747b5adfbce60571198fa57"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libsm-devel")
def _(self):
    return self.default_devel()
