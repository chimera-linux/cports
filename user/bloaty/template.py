pkgname = "bloaty"
pkgver = "1.1"
pkgrel = 9
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf", "protobuf"]
makedepends = [
    "abseil-cpp-devel",
    "capstone-devel",
    "protobuf-devel",
    "re2-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Size profiler for binaries"
license = "Apache-2.0"
url = "https://github.com/google/bloaty"
source = f"{url}/releases/download/v{pkgver}/bloaty-{pkgver}.tar.bz2"
sha256 = "a308d8369d5812aba45982e55e7c3db2ea4780b7496a5455792fb3dcba9abd6f"


def install(self):
    self.install_bin("build/bloaty")
