pkgname = "onetbb"
pkgver = "2022.0.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only"
url = "https://oneapi-src.github.io/oneTBB"
source = (
    f"https://github.com/oneapi-src/oneTBB/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "e8e89c9c345415b17b30a2db3095ba9d47647611662073f7fbf54ad48b7f3c2a"
# vis breaks symbols
hardening = []
# a lot of the tests can deadlock and it's a pain to figure out which to disable
options = ["!check", "linkundefver"]


@subpackage("onetbb-devel")
def _(self):
    return self.default_devel()
