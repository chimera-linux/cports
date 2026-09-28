pkgname = "onetbb"
pkgver = "2023.0.0"
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
sha256 = "f8767b971ec6aea25dde58ae0f593e94e7aa75a739a86f67967012f69e2199b1"
# vis breaks symbols
hardening = ["!vis"]
# a lot of the tests can deadlock and it's a pain to figure out which to disable
options = ["!check", "linkundefver"]


@subpackage("onetbb-devel")
def _(self):
    return self.default_devel()
