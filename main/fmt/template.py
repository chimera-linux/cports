pkgname = "fmt"
pkgver = "12.2.1"
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
sha256 = "870a49acec5bcdab236aeea834ebd7f0b8548a7d8cea33c996b6873a37f2d50c"
# CFI: test failures
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


# cmake shenanigans
@split("devel-static")
def _(self):
    self.depends = []

    return ["usr/lib/*.a"]


@split("devel")
def _(self):
    self.depends += [self.with_pkgver("fmt-devel-static")]

    return self.default_devel()
