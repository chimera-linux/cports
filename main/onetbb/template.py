pkgname = "onetbb"
pkgver = "2022.1.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DTBB4PY_BUILD=OFF",
    "-DTBB_STRICT=OFF",
    "-DTBB_TEST=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "hwloc-devel",
    "libucontext-devel",
    "linux-headers",
]
pkgdesc = "OneAPI Threading Building Blocks"
license = "GPL-2.0-only"
url = "https://oneapi-src.github.io/oneTBB"
source = (
    f"https://github.com/oneapi-src/oneTBB/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "ed067603ece0dc832d2881ba5c516625ac2522c665d95f767ef6304e34f961b5"
# vis breaks symbols
hardening = []
# a lot of the tests can deadlock and it's a pain to figure out which to disable
options = ["!check", "linkundefver"]


@subpackage("onetbb-devel")
def _(self):
    return self.default_devel()
