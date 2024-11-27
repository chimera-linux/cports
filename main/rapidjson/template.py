# header files only
pkgname = "rapidjson"
pkgver = "1.1.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DGTESTSRC_FOUND=ON",
    "-DGTEST_SOURCE_DIR=.",
    "-DRAPIDJSON_BUILD_DOC=OFF",
    "-DRAPIDJSON_BUILD_EXAMPLES=OFF",
    "-DRAPIDJSON_BUILD_CXX11=OFF",
]
make_check_args = ["-E", "valgrind_unittest"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "gtest-devel",
]
pkgdesc = "JSON parser/generator for C++"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://rapidjson.org"
source = (
    f"https://github.com/Tencent/rapidjson/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "bf7ced29704a1e696fbccf2a2b4ea068e7774fa37f6d7dd4039d0787f8bed98e"


def post_install(self):
    self.install_license("license.txt")
