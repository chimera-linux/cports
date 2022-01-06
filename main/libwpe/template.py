pkgname = "libwpe"
pkgver = "1.12.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["mesa-devel", "libxkbcommon-devel"]
pkgdesc = "General-purpose library for WPE WebKit"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://wpewebkit.org"
source = f"{url}/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "e8eeca228a6b4c36294cfb63f7d3ba9ada47a430904a5a973b3c99c96a44c18c"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libwpe-devel")
def _devel(self):
    return self.default_devel()
