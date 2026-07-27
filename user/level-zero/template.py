pkgname = "level-zero"
pkgver = "1.32.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=None",
    "-DSYSTEM_SPDLOG=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "opencl-headers",
    "pkgconf",
]
makedepends = ["spdlog-devel"]
pkgdesc = "OneAPI Level Zero loader"
license = "MIT"
url = "https://github.com/oneapi-src/level-zero"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b658d3be89b2ea3c5e6b3214592acb58a4875e738184b1a4cc7e9cf878b5f7b9"
# disabled test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("level-zero-headers")
def _(self):
    self.subdesc = "specification headers"

    return ["usr/include"]
