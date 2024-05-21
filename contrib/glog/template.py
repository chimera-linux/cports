pkgname = "glog"
pkgver = "0.7.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DWITH_GFLAGS=ON",
    "-DWITH_PKGCONFIG=ON",
    "-DWITH_TLS=ON",
]
# fails to check backtrace
make_check_args = ["-E", "symbolize"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "gflags-devel",
    "gflags-devel-static",  # cmake detection
    "gtest-devel",
]
pkgdesc = "C++ implementation of the Google logging module"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://github.com/google/glog"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "375106b5976231b92e66879c1a92ce062923b9ae573c42b56ba28b112ee4cc11"
# fails
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("glog-devel")
def _devel(self):
    self.depends += ["gflags-devel-static"]
    return self.default_devel()
