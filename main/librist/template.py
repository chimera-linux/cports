pkgname = "librist"
pkgver = "0.2.11"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://code.videolan.org/rist/librist"
source = f"https://code.videolan.org/rist/librist/-/archive/v{pkgver}/librist-v{pkgver}.tar.bz2"
sha256 = "f254842900a9dd20fb477b05ea0cce3ec1a8004d85177eef2408eefddca68b86"
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
