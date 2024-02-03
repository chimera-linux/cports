pkgname = "libwpe"
pkgver = "1.14.2"
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
sha256 = "8ae38022c50cb340c96fdbee1217f1e46ab57fbc1c8ba98142565abbedbe22ef"
# FIXME cfi (wpe_view_backend_create_with_backend_interface)
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libwpe-devel")
def _devel(self):
    return self.default_devel()
