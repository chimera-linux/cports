pkgname = "libpciaccess"
pkgver = "0.18.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "X11 PCI access library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/{pkgname}-{pkgver}.tar.xz"
sha256 = "4af43444b38adb5545d0ed1c2ce46d9608cc47b31c2387fc5181656765a6fa76"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libpciaccess-devel")
def _devel(self):
    return self.default_devel()
