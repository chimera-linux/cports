pkgname = "svt-av1"
pkgver = "3.0.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_STYLE=Release",
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_TESTING=OFF",
    "-DSVT_AV1_LTO=OFF",
    "-DUSE_CPUINFO=LOCAL",
]
hostmakedepends = [
    "cmake",
    "nasm",
    "ninja",
    "pkgconf",
]
checkdepends = ["python"]
pkgdesc = "AOMedia Scalable Video Technology AV1 Encoder/Decoder"
license = "BSD-3-Clause-Clear"
url = "https://gitlab.com/AOMediaCodec/SVT-AV1"
source = [
    f"{url}/-/archive/v{pkgver}/SVT-AV1-v{pkgver}.tar.gz",
    "https://github.com/pytorch/cpuinfo/archive/39ea79a3c132f4e678695c579ea9353d2bd29968.tar.gz",
]
source_paths = [".", "third_party/cpuinfo"]
sha256 = [
    "5af7f4376aa00a4dee32df04be1cdd1983c9940bcc019ee6b29bb8a216bae2f8",
    "6774168f35ddf535299fc6db6531f7035f1d709266d9f1acae0b242eeb98ef5c",
]
# FIXME int: muloverflow in svt_av1_find_best_sub_pixel_tree for certain encodes
hardening = ["vis", "cfi", "!int"]
# needs patching+clones of a bunch of stuff
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("svt-av1-devel")
def _(self):
    return self.default_devel()


@subpackage("svt-av1-libs")
def _(self):
    return self.default_libs()
