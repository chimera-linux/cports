pkgname = "libsm"
pkgver = "1.2.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf", "xorg-util-macros"]
makedepends = ["libice-devel", "util-linux-uuid-devel", "xtrans"]
pkgdesc = "X session management library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libSM-{pkgver}.tar.gz"
sha256 = "166b4b50d606cdd83f1ddc61b5b9162600034f848b3e32ccbb0e63536b7d6cdd"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libsm-devel")
def _(self):
    return self.default_devel()
