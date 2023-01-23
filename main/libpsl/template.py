pkgname = "libpsl"
pkgver = "0.21.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "python"]
makedepends = ["icu-devel", "libidn2-devel", "libunistring-devel"]
pkgdesc = "Public Suffix List library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://rockdaboot.github.io/libpsl"
source = f"https://github.com/rockdaboot/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "ac6ce1e1fbd4d0254c4ddb9d37f1fa99dec83619c1253328155206b896210d4c"
hardening = ["vis", "cfi"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libpsl-devel")
def _devel(self):
    return self.default_devel()
