pkgname = "spdlog"
pkgver = "1.16.0"
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
sha256 = "8741753e488a78dd0d0024c980e1fb5b5c85888447e309d9cb9d949bdb52aa3e"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("spdlog-devel")
def _(self):
    return self.default_devel()
