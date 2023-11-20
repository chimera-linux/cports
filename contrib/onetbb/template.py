pkgname = "onetbb"
pkgver = "2021.11.0"
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
sha256 = "782ce0cab62df9ea125cdea253a50534862b563f1d85d4cda7ad4e77550ac363"
# vis breaks symbols
hardening = []
# a lot of the tests can deadlock and it's a pain to figure out which to disable
options = ["!check", "linkundefver"]


@subpackage("onetbb-devel")
def _devel(self):
    return self.default_devel()
