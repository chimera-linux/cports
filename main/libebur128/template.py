pkgname = "libebur128"
pkgver = "1.2.6"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_TESTS=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Library implementing the EBU R128 loudness standard"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/jiixyj/libebur128"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "baa7fc293a3d4651e244d8022ad03ab797ca3c2ad8442c43199afe8059faa613"
# vis: missing symbols
hardening = []
# tests need misc wav files from somewhere
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libebur128-devel")
def _(self):
    return self.default_devel()
