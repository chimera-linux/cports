pkgname = "libwpe"
pkgver = "1.16.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["mesa-devel", "libxkbcommon-devel"]
pkgdesc = "General-purpose library for WPE WebKit"
license = "BSD-2-Clause"
url = "https://wpewebkit.org"
source = f"{url}/releases/libwpe-{pkgver}.tar.xz"
sha256 = "960bdd11c3f2cf5bd91569603ed6d2aa42fd4000ed7cac930a804eac367888d7"
# CFI: wpe_view_backend_create_with_backend_interface
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libwpe-devel")
def _(self):
    return self.default_devel()
