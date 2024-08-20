pkgname = "librist"
pkgver = "0.2.10"
pkgrel = 1
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
sha256 = "c4a2c1bf62310fa1621b1a66140aa6fda8498a80fa5cc73d32335aa57015f7f5"
hardening = ["vis", "!cfi"]
# multicast tests cannot make socket in sandbox
# also don't build with redefined free
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("librist-devel")
def _(self):
    return self.default_devel()


@subpackage("librist-progs")
def _(self):
    return self.default_progs()
