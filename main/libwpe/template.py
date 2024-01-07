pkgname = "libwpe"
pkgver = "1.14.1"
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
sha256 = "b1d0cdcf0f8dbb494e65b0f7913e357106da9a0d57f4fbb7b9d1238a6dbe9ade"
# FIXME cfi (wpe_view_backend_create_with_backend_interface)
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libwpe-devel")
def _devel(self):
    return self.default_devel()
