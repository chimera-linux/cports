pkgname = "libavif"
pkgver = "1.3.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DAVIF_BUILD_APPS=ON",
    "-DAVIF_BUILD_GDK_PIXBUF=ON",
    "-DAVIF_CODEC_DAV1D=SYSTEM",
    "-DAVIF_CODEC_AOM=SYSTEM",
    "-DAVIF_LIBYUV=OFF",
    "-DAVIF_BUILD_TESTS=ON",
    "-DAVIF_GTEST=SYSTEM",
    "-DAVIF_ENABLE_GTEST=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "dav1d-devel",
    "gdk-pixbuf-devel",
    "gtest-devel",
    "libaom-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libwebp-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["bash"]
pkgdesc = "Library for encoding and decoding .avif files"
license = "BSD-2-Clause"
url = "https://github.com/AOMediaCodec/libavif"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    "https://github.com/kmurray/libargparse/archive/ee74d1b53bd680748af14e737378de57e2a0a954.tar.gz",
]
source_paths = [".", "ext/libargparse"]
sha256 = [
    "0a545e953cc049bf5bcf4ee467306a2f113a75110edf59e61248873101cd26c1",
    "7727b0498851e5b6a6fcd734eb667a8a231897e2c86a357aec51cc0664813060",
]
hardening = ["!vis", "!cfi"]
# fails since libpng update, check again for 1.2
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libavif-devel")
def _(self):
    return self.default_devel()


@subpackage("libavif-progs")
def _(self):
    return self.default_progs()
