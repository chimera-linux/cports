pkgname = "spdlog"
pkgver = "1.17.0"
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
checkdepends = ["tzdb"]
pkgdesc = "C++ logging library"
license = "MIT"
url = "https://github.com/gabime/spdlog"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d8862955c6d74e5846b3f580b1605d2428b11d97a410d86e2fb13e857cd3a744"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("spdlog-devel")
def _(self):
    return self.default_devel()
