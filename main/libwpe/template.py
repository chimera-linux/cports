pkgname = "libwpe"
pkgver = "1.16.0"
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
sha256 = "c7f3a3c6b3d006790d486dc7cceda2b6d2e329de07f33bc47dfc53f00f334b2a"
# FIXME cfi (wpe_view_backend_create_with_backend_interface)
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libwpe-devel")
def _devel(self):
    return self.default_devel()
