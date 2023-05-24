pkgname = "libslirp"
pkgver = "4.7.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["glib-devel", "linux-headers"]
pkgdesc = "General purpose TCP-IP emulator"
maintainer = "eater <=@eater.me>"
license = "BSD-3-Clause"
url = "https://gitlab.freedesktop.org/slirp/libslirp"
source = f"https://gitlab.freedesktop.org/slirp/libslirp/-/archive/v{pkgver}/libslirp-v{pkgver}.tar.gz"
sha256 = "9398f0ec5a581d4e1cd6856b88ae83927e458d643788c3391a39e61b75db3d3b"


@subpackage("libslirp-devel")
def _devel(self):
    return self.default_devel()
