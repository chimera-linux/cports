pkgname = "libxcb"
pkgver = "1.16"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-build-docs", "--enable-xinput", "--enable-xkb"]
hostmakedepends = ["pkgconf", "libtool", "xorg-util-macros", "xcbproto"]
makedepends = ["xcbproto", "libxdmcp-devel", "libxau-devel"]
pkgdesc = "X protocol C language binding"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"https://xorg.freedesktop.org/archive/individual/lib/libxcb-{pkgver}.tar.xz"
sha256 = "4348566aa0fbf196db5e0a576321c65966189210cb51328ea2bb2be39c711d71"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxcb-devel")
def _devel(self):
    self.depends += ["xcbproto"]
    return self.default_devel(extra=["usr/share/doc"])


configure_gen = []
