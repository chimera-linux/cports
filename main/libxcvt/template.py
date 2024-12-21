pkgname = "libxcvt"
pkgver = "0.1.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Library to handle VESA CVT modeline generation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xkbcommon.org"
source = f"$(XORG_SITE)/lib/libxcvt-{pkgver}.tar.xz"
sha256 = "a929998a8767de7dfa36d6da4751cdbeef34ed630714f2f4a767b351f2442e01"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxcvt-devel")
def _(self):
    return self.default_devel()


@subpackage("libxcvt-progs")
def _(self):
    return self.default_progs()
