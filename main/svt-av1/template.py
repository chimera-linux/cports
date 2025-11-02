pkgname = "svt-av1"
pkgver = "3.1.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_STYLE=Release",
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_TESTING=OFF",
    "-DSVT_AV1_LTO=OFF",
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
source = f"{url}/-/archive/v{pkgver}/SVT-AV1-v{pkgver}.tar.gz"
sha256 = "d0d73bfea42fdcc1222272bf2b0e2319e9df5574721298090c3d28315586ecb1"
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
