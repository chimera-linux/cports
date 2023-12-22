pkgname = "libjxl"
pkgver = "0.9.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_TESTING=ON",
    "-DJPEGXL_ENABLE_BENCHMARK=OFF",
    "-DJPEGXL_ENABLE_JPEGLI=OFF",
    "-DJPEGXL_ENABLE_PLUGINS=OFF",
    "-DJPEGXL_ENABLE_SJPEG=OFF",
    "-DJPEGXL_ENABLE_SKCMS=OFF",
    "-DJPEGXL_FORCE_SYSTEM_BROTLI=ON",
    "-DJPEGXL_FORCE_SYSTEM_GTEST=ON",
    "-DJPEGXL_FORCE_SYSTEM_HWY=ON",
    "-DJPEGXL_FORCE_SYSTEM_LCMS2=ON",
    f"-DJPEGXL_VERSION={pkgver}",
]
hostmakedepends = [
    "asciidoc",
    "cmake",
    "libxml2-progs",
    "ninja",
    "pkgconf",
]
makedepends = [
    "brotli-devel",
    "gflags-devel",
    "giflib-devel",
    "gtest-devel",
    "highway-devel",
    "lcms2-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "openexr-devel",
]
pkgdesc = "Reference JpegXL implementation"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://github.com/libjxl/libjxl"
_testdata = "6c943639760d38c91609f4a72e46c2bc19984a0a"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/libjxl/testdata/archive/{_testdata}.tar.gz",
]
source_paths = [".", "testdata"]
sha256 = [
    "d83bbe188d8fa9725bb75109c922c37fcff8c3b802808f3a6c2c14aaf8337d9f",
    "bb1ad522df427aaee6f3fc5b67d0e4a85e59ae291450b1bedcca1ccb3bb75e99",
]
# FIXME: a bunch of cfi test failures
# vis also broken
hardening = ["!vis"]


# FIXME
if self.profile().arch == "riscv64":
    configure_args += ["-DBUILD_TESTING=OFF"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libjxl-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libjxl-progs")
def _progs(self):
    return self.default_progs()
