pkgname = "libtsm"
pkgver = "4.6.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["check-devel", "libxkbcommon-devel"]
pkgdesc = "Terminal emulator state machine"
license = "MIT"
url = "https://github.com/kmscon/libtsm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5c64411fd558aa004170af9a04c12c3095e593b9e38a2fec7da1dafa7793dbb7"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libtsm-devel")
def _(self):
    return self.default_devel()
