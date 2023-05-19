pkgname = "libpsl"
pkgver = "0.21.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "python"]
makedepends = ["icu-devel", "libidn2-devel", "libunistring-devel"]
pkgdesc = "Public Suffix List library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://rockdaboot.github.io/libpsl"
source = f"https://github.com/rockdaboot/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "e35991b6e17001afa2c0ca3b10c357650602b92596209b7492802f3768a6285f"
hardening = ["vis", "cfi"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libpsl-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
