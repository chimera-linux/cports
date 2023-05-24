pkgname = "libxcb"
pkgver = "1.15"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-build-docs", "--enable-xinput", "--enable-xkb"]
hostmakedepends = ["pkgconf", "libtool", "xorg-util-macros", "xcbproto"]
makedepends = ["xcbproto", "libxdmcp-devel", "libxau-devel"]
pkgdesc = "X protocol C language binding"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"{url}/dist/{pkgname}-{pkgver}.tar.xz"
sha256 = "cc38744f817cf6814c847e2df37fcb8997357d72fa4bcbc228ae0fe47219a059"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxcb-devel")
def _devel(self):
    self.depends += ["xcbproto"]
    return self.default_devel(extra=["usr/share/doc"])


configure_gen = []
