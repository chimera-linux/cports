pkgname = "librist"
pkgver = "0.2.7"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "ninja",
    "pkgconf",
]
makedepends = [
    "cjson-devel",
    "cmocka-devel",
    "linux-headers",
    "mbedtls-devel",
]
pkgdesc = "Reliable Internet Stream Transport"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-2-Clause"
url = "https://code.videolan.org/rist/librist"
source = f"https://code.videolan.org/rist/librist/-/archive/v{pkgver}/librist-v{pkgver}.tar.bz2"
sha256 = "7adf2ef9e61e909020df6d22a38b4416380809e655a3f947fcd548b9af115603"
# FIXME: cfi
hardening = ["vis"]
# multicast tests cannot make socket in sandbox
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("librist-devel")
def _devel(self):
    return self.default_devel()


@subpackage("librist-progs")
def _progs(self):
    return self.default_progs()
