pkgname = "fmt"
pkgver = "11.1.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
]
# FIXME: random musl issues
# format hangs on ppc64
make_check_args = ["-E", "(format|chrono|unicode|xchar)"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "python",
]
pkgdesc = "Formatting library for C++"
license = "MIT"
url = "https://fmt.dev/latest/index.html"
source = (
    f"https://github.com/fmtlib/fmt/releases/download/{pkgver}/fmt-{pkgver}.zip"
)
sha256 = "49b039601196e1a765e81c5c9a05a61ed3d33f23b3961323d7322e4fe213d3e6"
# CFI: test failures
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("fmt-devel")
def _(self):
    return self.default_devel()
