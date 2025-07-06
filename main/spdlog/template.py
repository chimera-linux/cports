pkgname = "spdlog"
pkgver = "1.15.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DSPDLOG_FMT_EXTERNAL=ON",
    "-DSPDLOG_BUILD_SHARED=ON",
    "-DSPDLOG_BUILD_EXAMPLE=OFF",
    "-DSPDLOG_BUILD_TESTS=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["catch2-devel", "elogind-devel", "fmt-devel"]
pkgdesc = "C++ logging library"
license = "MIT"
url = "https://github.com/gabime/spdlog"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "15a04e69c222eb6c01094b5c7ff8a249b36bb22788d72519646fb85feb267e67"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("spdlog-devel")
def _(self):
    return self.default_devel()
