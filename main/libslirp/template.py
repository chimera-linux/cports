pkgname = "libslirp"
pkgver = "4.8.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["glib-devel", "linux-headers"]
pkgdesc = "General purpose TCP-IP emulator"
maintainer = "eater <=@eater.me>"
license = "BSD-3-Clause"
url = "https://gitlab.freedesktop.org/slirp/libslirp"
source = f"{url}/-/archive/v{pkgver}/libslirp-v{pkgver}.tar.gz"
sha256 = "2a98852e65666db313481943e7a1997abff0183bd9bea80caec1b5da89fda28c"


def post_install(self):
    self.install_license("COPYRIGHT")


@subpackage("libslirp-devel")
def _(self):
    return self.default_devel()
