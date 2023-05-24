pkgname = "libxcvt"
pkgver = "0.1.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Library to handle VESA CVT modeline generation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xkbcommon.org"
source = f"$(XORG_SITE)/lib/{pkgname}-{pkgver}.tar.xz"
sha256 = "0561690544796e25cfbd71806ba1b0d797ffe464e9796411123e79450f71db38"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxcvt-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libxcvt-progs")
def _progs(self):
    return self.default_progs()
