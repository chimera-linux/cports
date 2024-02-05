pkgname = "libpciaccess"
pkgver = "0.18"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "X11 PCI access library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/{pkgname}-{pkgver}.tar.xz"
sha256 = "5461b0257d495254346f52a9c329b44b346262663675d3fecdb204a7e7c262a9"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libpciaccess-devel")
def _devel(self):
    return self.default_devel()
