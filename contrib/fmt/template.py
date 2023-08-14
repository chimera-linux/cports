pkgname = "fmt"
pkgver = "10.1.0"
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
sha256 = "d725fa83a8b57a3cedf238828fa6b167f963041e8f9f7327649bddc68ae316f4"
# FIXME: cfi test failures
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSE.rst")


@subpackage("fmt-devel")
def _devel(self):
    return self.default_devel()
