pkgname = "libwpe"
pkgver = "1.16.3"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["mesa-devel", "libxkbcommon-devel"]
pkgdesc = "General-purpose library for WPE WebKit"
license = "BSD-2-Clause"
url = "https://wpewebkit.org"
source = f"{url}/releases/libwpe-{pkgver}.tar.xz"
sha256 = "c880fa8d607b2aa6eadde7d6d6302b1396ebc38368fe2332fa20e193c7ee1420"
# CFI: wpe_view_backend_create_with_backend_interface
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libwpe-devel")
def _(self):
    return self.default_devel()
