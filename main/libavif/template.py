pkgname = "libavif"
pkgver = "1.0.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DAVIF_BUILD_APPS=ON",
    "-DAVIF_BUILD_GDK_PIXBUF=ON",
    "-DAVIF_CODEC_DAV1D=ON",
    "-DAVIF_CODEC_AOM=ON",
    "-DAVIF_BUILD_TESTS=OFF",
    "-DAVIF_ENABLE_WERROR=OFF",
    "-DAVIF_ENABLE_GTEST=OFF",
]
make_check_target = "avif_test_all"
hostmakedepends = ["cmake", "ninja", "pkgconf", "gdk-pixbuf-devel"]
makedepends = [
    "gdk-pixbuf-devel",
    "dav1d-devel",
    "libaom-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "zlib-devel",
]
pkgdesc = "Library for encoding and decoding .avif files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/AOMediaCodec/libavif"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "dc56708c83a4b934a8af2b78f67f866ba2fb568605c7cf94312acf51ee57d146"
hardening = ["!cfi"]  # TODO when we have tests
# doesn't pass with current dependencies, needs gtest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libavif-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libavif-progs")
def _progs(self):
    return self.default_progs()
