pkgname = "libjxl"
pkgver = "0.9.2"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_TESTING=ON",
    "-DJPEGXL_ENABLE_BENCHMARK=OFF",
    "-DJPEGXL_ENABLE_JPEGLI=OFF",
    "-DJPEGXL_ENABLE_PLUGINS=ON",
    "-DJPEGXL_ENABLE_PLUGIN_GIMP210=OFF",
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
    "gdk-pixbuf-devel",
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
_testdata = "ff8d743aaba05b3014f17e5475e576242fa979fc"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/libjxl/testdata/archive/{_testdata}.tar.gz",
]
source_paths = [".", "testdata"]
sha256 = [
    "bf28e411d84c50578ab74107cdd624e099313129883a43907c261e8116a11b3b",
    "9c45a108df32a002a69465df896d33acf77d97c88fb59dffa0dff5628370e96f",
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
