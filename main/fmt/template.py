pkgname = "fmt"
pkgver = "11.2.0"
pkgrel = 1
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
sha256 = "203eb4e8aa0d746c62d8f903df58e0419e3751591bb53ff971096eaa0ebd4ec3"
# CFI: test failures
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("fmt-devel")
def _(self):
    return self.default_devel()
