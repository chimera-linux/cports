pkgname = "spdlog"
pkgver = "1.14.1"
pkgrel = 1
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
sha256 = "1586508029a7d0670dfcb2d97575dcdc242d3868a259742b69f100801ab4e16b"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("spdlog-devel")
def _(self):
    return self.default_devel()
