pkgname = "libtsm"
pkgver = "4.7.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["check-devel", "libxkbcommon-devel"]
pkgdesc = "Terminal emulator state machine"
license = "MIT"
url = "https://github.com/kmscon/libtsm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "40d7f11698f0ce87af8da67a3142ee9f02e2b5d914f8ad83aa080e052fe1ae2b"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libtsm-devel")
def _(self):
    return self.default_devel()
