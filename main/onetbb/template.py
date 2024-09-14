pkgname = "onetbb"
pkgver = "2021.13.0"
pkgrel = 1
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
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only"
url = "https://oneapi-src.github.io/oneTBB"
source = (
    f"https://github.com/oneapi-src/oneTBB/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "3ad5dd08954b39d113dc5b3f8a8dc6dc1fd5250032b7c491eb07aed5c94133e1"
# vis breaks symbols
hardening = []
# a lot of the tests can deadlock and it's a pain to figure out which to disable
options = ["!check", "linkundefver"]


@subpackage("onetbb-devel")
def _(self):
    return self.default_devel()
