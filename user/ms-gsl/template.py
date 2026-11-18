pkgname = "ms-gsl"
pkgver = "5.0.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DGSL_CXX_STANDARD=17",
    "-DGSL_INSTALL=ON",
    "-DGSL_TEST=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["gtest-devel"]
pkgdesc = "Microsoft Guidelines Support Library"
license = "MIT"
url = "https://github.com/microsoft/GSL"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "733a87a7eea56db075ee060735ba7616a27c1c55955f264d5473bf9e83294ad0"
# GTest death tests expand musl's self-referencing stderr macro under -Werror.
tool_flags = {"CXXFLAGS": ["-Wno-disabled-macro-expansion"]}


def post_install(self):
    self.install_license("LICENSE")
