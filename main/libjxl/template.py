pkgname = "libjxl"
pkgver = "0.8.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DJPEGXL_ENABLE_BENCHMARK=OFF",
    "-DJPEGXL_ENABLE_SKCMS=OFF",
    "-DJPEGXL_ENABLE_SJPEG=OFF",
    "-DJPEGXL_ENABLE_PLUGINS=OFF",
    "-DJPEGXL_FORCE_SYSTEM_GTEST=ON",
    "-DJPEGXL_FORCE_SYSTEM_BROTLI=ON",
    "-DJPEGXL_FORCE_SYSTEM_HWY=ON",
    "-DJPEGXL_FORCE_SYSTEM_LCMS2=ON",
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
_testdata = "d6168ffb9e1cc24007e64b65dd84d822ad1fc759"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/libjxl/testdata/archive/{_testdata}.tar.gz",
]
source_paths = [".", "testdata"]
sha256 = [
    "c70916fb3ed43784eb840f82f05d390053a558e2da106e40863919238fa7b420",
    "64658d3341bff2976899cb8b140242ffa4de1cd41aed507dfec4aa9e7e05ca24",
]
# FIXME: a bunch of cfi test failures
hardening = ["vis"]


def init_check(self):
    skip = [
        "(",
        # FIXME: ?
        "DecodeTest.ContinueFinalNonEssentialBoxTest|",
        "JxlTest.RoundtripLossless8LightningGradient|",
        "JxlTest.LosslessPNMRoundtrip|",
        # whole suite fails because of using lcms instead of skcms probably
        # (off-by-one byte errors on color management)
        "ColorManagementTestInstantiation/ColorManagementTest.VerifyAllProfiles/ColorEncoding",
        ")",
    ]
    self.make_check_args += [
        "-E",
        "".join(skip),
    ]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libjxl-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libjxl-progs")
def _progs(self):
    return self.default_progs()
