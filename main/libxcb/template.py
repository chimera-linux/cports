pkgname = "libxcb"
pkgver = "1.17.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-build-docs", "--enable-xinput", "--enable-xkb"]
# broken reconf
configure_gen = []
hostmakedepends = ["pkgconf", "libtool", "xorg-util-macros", "xcbproto"]
makedepends = ["xcbproto", "libxdmcp-devel", "libxau-devel"]
pkgdesc = "X protocol C language binding"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"https://xorg.freedesktop.org/archive/individual/lib/libxcb-{pkgver}.tar.xz"
sha256 = "599ebf9996710fea71622e6e184f3a8ad5b43d0e5fa8c4e407123c88a59a6d55"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxcb-devel")
def _devel(self):
    self.depends += ["xcbproto"]
    return self.default_devel(extra=["usr/share/doc"])
