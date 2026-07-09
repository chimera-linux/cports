pkgname = "lager"
pkgver = "0.1.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-Dlager_BUILD_EXAMPLES=OFF",
    "-Dlager_BUILD_DEBUGGER_EXAMPLES=OFF",
    "-Dlager_BUILD_TESTS=OFF",
]
make_check_target = "check"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
depends = [
    "boost-devel",
    "immer",
    "zug",
]
checkdepends = [
    "catch2-devel",
    *depends,
]
pkgdesc = "C++ library for transducers"
license = "BSL-1.0"
url = "https://sinusoid.es/lager"
source = (
    f"https://github.com/arximboldi/lager/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "55d3442d2d4306aad78fa2af5d3db01af65f4fdbfc58c4620fba13dbde82e599"
# needs old catch2, no patch
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
