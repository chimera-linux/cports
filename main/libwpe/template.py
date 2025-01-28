pkgname = "libwpe"
pkgver = "1.16.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["mesa-devel", "libxkbcommon-devel"]
pkgdesc = "General-purpose library for WPE WebKit"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://wpewebkit.org"
source = f"{url}/releases/libwpe-{pkgver}.tar.xz"
sha256 = "9cca60f2c4393ea0de53c675ebc3cdbe9c5aa249259dd1d6d81a49b052d37481"
# CFI: wpe_view_backend_create_with_backend_interface
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libwpe-devel")
def _(self):
    return self.default_devel()
