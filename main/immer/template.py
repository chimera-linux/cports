pkgname = "immer"
pkgver = "0.9.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DDISABLE_WERROR=ON"]
make_check_target = "check"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
depends = [
    "boost-devel",
    "gc-devel",
]
checkdepends = [
    "catch2-devel",
    "fmt-devel",
    *depends,
]
pkgdesc = "C++ library for persistent and immutable data structures"
license = "BSL-1.0"
url = "https://sinusoid.es/immer"
source = (
    f"https://github.com/arximboldi/immer/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "b18b92ba60ec3186dc36ef671d3c2ae542cbb63eb6dc0e258476c6111a67c971"
# read() in fortify clashes with test code
tool_flags = {"CXXFLAGS": ["-Wno-c2y-extensions", "-U_FORTIFY_SOURCE"]}


def post_install(self):
    self.install_license("LICENSE")
