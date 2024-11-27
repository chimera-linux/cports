pkgname = "glog"
pkgver = "0.7.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DWITH_GFLAGS=ON",
    "-DWITH_PKGCONFIG=ON",
    "-DWITH_TLS=ON",
]
# fails to check backtrace
make_check_args = ["-E", "symbolize", "-j1"]
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/google/glog"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "00e4a87e87b7e7612f519a41e491f16623b12423620006f59f5688bfd8d13b08"
# fails
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("glog-devel")
def _(self):
    self.depends += ["gflags-devel-static"]
    return self.default_devel()
