pkgname = "fmt"
pkgver = "10.2.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
]
# FIXME: random musl issues
make_check_args = ["-E", "(chrono|format|unicode|xchar)"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "python",
]
pkgdesc = "Formatting library for C++"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://fmt.dev/latest/index.html"
source = (
    f"https://github.com/fmtlib/fmt/releases/download/{pkgver}/fmt-{pkgver}.zip"
)
sha256 = "8a942861a94f8461a280f823041cde8f620a6d8b0e0aacc98c15bb5a9dd92399"
# FIXME: cfi test failures
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("fmt-devel")
def _devel(self):
    return self.default_devel()
