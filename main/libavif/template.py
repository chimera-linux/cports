pkgname = "libavif"
pkgver = "1.1.1"
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
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "914662e16245e062ed73f90112fbb4548241300843a7772d8d441bb6859de45b"
hardening = ["!vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libavif-devel")
def _(self):
    return self.default_devel()


@subpackage("libavif-progs")
def _(self):
    return self.default_progs()
