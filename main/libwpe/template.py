pkgname = "libwpe"
pkgver = "1.14.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["mesa-devel", "libxkbcommon-devel"]
pkgdesc = "General-purpose library for WPE WebKit"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://wpewebkit.org"
source = f"{url}/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "c073305bbac5f4402cc1c8a4753bfa3d63a408901f86182051eaa5a75dd89c00"
hardening = ["vis", "cfi"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libwpe-devel")
def _devel(self):
    return self.default_devel()
