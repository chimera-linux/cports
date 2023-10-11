pkgname = "librist"
pkgver = "0.2.9"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dtest=false",
]
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
sha256 = "3fb9dacd4683c31f5f3efb152615d993ec6769f60f25009f5f1dc022483348a9"
# FIXME: cfi
hardening = ["vis"]
# multicast tests cannot make socket in sandbox
# also don't build with redefined free
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("librist-devel")
def _devel(self):
    return self.default_devel()


@subpackage("librist-progs")
def _progs(self):
    return self.default_progs()
