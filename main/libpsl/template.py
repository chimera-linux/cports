pkgname = "libpsl"
pkgver = "0.21.5"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "ninja", "pkgconf"]
makedepends = ["icu-devel", "libidn2-devel", "libunistring-devel"]
pkgdesc = "Public Suffix List library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://rockdaboot.github.io/libpsl"
source = f"https://github.com/rockdaboot/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "1dcc9ceae8b128f3c0b3f654decd0e1e891afc6ff81098f227ef260449dae208"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libpsl-devel")
def _devel(self):
    return self.default_devel()
