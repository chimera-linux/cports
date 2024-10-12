pkgname = "libsm"
pkgver = "1.2.4"
pkgrel = 2
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf", "xorg-util-macros"]
makedepends = ["libice-devel", "libuuid-devel", "xtrans"]
pkgdesc = "X session management library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libSM-{pkgver}.tar.gz"
sha256 = "51464ce1abce323d5b6707ceecf8468617106e1a8a98522f8342db06fd024c15"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libsm-devel")
def _(self):
    return self.default_devel()
