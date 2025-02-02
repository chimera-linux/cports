pkgname = "spdlog"
pkgver = "1.15.1"
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
maintainer = "avgwst <avgwst@tutanota.de>"
license = "MIT"
url = "https://github.com/gabime/spdlog"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "25c843860f039a1600f232c6eb9e01e6627f7d030a2ae5e232bdd3c9205d26cc"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("spdlog-devel")
def _(self):
    return self.default_devel()
