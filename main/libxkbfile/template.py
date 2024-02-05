pkgname = "libxkbfile"
pkgver = "1.1.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["xorgproto", "libx11-devel"]
pkgdesc = "Xkbfile library from X.org"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/{pkgname}-{pkgver}.tar.xz"
sha256 = "a9b63eea997abb9ee6a8b4fbb515831c841f471af845a09de443b28003874bec"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxkbfile-devel")
def _devel(self):
    return self.default_devel()
